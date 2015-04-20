#!/usr/local/bin/python2.7
# encoding: utf-8
'''
bin.generate_app -- shortdesc

bin.generate_app is a description

It defines classes_and_methods

@author:     Tim1

@copyright:  2015 organization_name. All rights reserved.

@license:    license

'''

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import os
import sys

# add prject to PYTHON_PATH
app_gen_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
if app_gen_dir not in sys.path:
    sys.path.append(app_gen_dir)

from generator import app_generator
from generator.manage import Manager

__all__ = []
__version__ = 0.1
__date__ = '2015-03-25'
__updated__ = '2015-03-25'

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by Tim1 on %s.
  Copyright 2015 Tim1 E2. All rights reserved.

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument('--new', dest='generate_new', action='store_true', help="generate a new test application, regenerate database and create a test user, same as -md --migrate --createsuperuser")
        parser.add_argument('-m', '--rewrite-migrations', dest='rewrite_migrations', action='store_true', help="don't backup migrations when generating, old migrations will be overwritten")
        parser.add_argument('-d', '--rewrite-database', dest='rewrite_db', action='store_true', help="don't backup database when generating, old database will be overwritten")
        parser.add_argument('--migrate', dest='migrate', action='store_true', help="do makemigrations and migrate the database")
        parser.add_argument('--createsuperuser', dest='create_super_user', action='store_true', help="add a test super user username=a, password=a, email=test@test.com")
        parser.add_argument('--runserver', dest='runserver', action='store_true', help="start the server")
        parser.add_argument(dest="xml_path", help="path to xml model file", metavar="xml_path")
        parser.add_argument(dest="dest_path", help="path to project destination folder", metavar="dest_path")
        
        # Process arguments
        args = parser.parse_args()

        xml_path = args.xml_path
        dest_path = args.dest_path
        migrate = args.migrate
        create_super_user = args.create_super_user
        runserver = args.runserver
        rewrite_migrations = args.rewrite_migrations
        rewrite_db = args.rewrite_db
        
        if args.generate_new:
            rewrite_migrations=True
            rewrite_db=True
            migrate=True
            create_super_user=True

        if not os.path.exists(xml_path):
            raise Exception('Provide a valid path to xml model file.')
        if not os.path.isfile(xml_path):
            raise Exception('Provide a valid path to xml model file.')
        
        if not os.path.exists(dest_path):
            raise Exception('Provide a valid path to project destination folder.')
        if not os.path.isdir(dest_path):
            raise Exception('Provide a valid path to project destination folder.')
        
        print('---generating application---')
        
        app_model = app_generator.generate_app_from_xml(path=dest_path, 
                                                        xml_model_path=xml_path, 
                                                        rewrite_db=rewrite_db, 
                                                        rewrite_migrations=rewrite_migrations)
        
        print('---application generated---')
        
        if migrate or create_super_user or runserver:
            project_name = app_model.app_name.replace(' ', '_')
            project_path = os.path.join(dest_path, project_name)
            manager = Manager(project_path, project_name)
            
            if migrate:
                print('---migrating database---')
                manager.migrate_database()
            if create_super_user:
                print('---adding test super user---')
                print('username=a')
                print('password=a')
                print('email=test@test.com')
                manager.create_super_user(username='a', password='a')
            if runserver:
                print('---starting server---')
                manager.run_server()
        
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
    