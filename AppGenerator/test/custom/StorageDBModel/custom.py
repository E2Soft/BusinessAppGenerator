

"""
	Created: 2015-04-06 13:23:27.478800
	
	@author: Milos
	
	EDIT THESE FUNCTIONS TO IMPLEMENT CUSTOM OPERATIONS
	FOR YOUR APPLICATION.
	
"""





from collections import OrderedDict
import json
from time import strftime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.platypus.flowables import Spacer

from business_app.models import Item


@login_required(login_url="/")
def Popust(request):
#TODO:Implement this view
	for item in Item.objects.all():
		item.pojedinacnaCena = item.pojedinacnaCena - (item.pojedinacnaCena * 0.1) # -10%
		item.save()
	return render(request, 'custom/discount.html')

@login_required(login_url="/")
def Popis(request):
#TODO:Implement this view
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
	doc.pagesize = landscape(A4)
	elements = []
	
	header = ["Name","Code","Price","Amount"]
	allitems = [[p.nazivArtikal, p.sifraArtikal, p.pojedinacnaCena, p.kolicina] for p in Item.objects.all()]
	
	data = []
	data.append(header)
	
	for p in allitems:
		data.append(p)
	
	#TODO: Get this line right instead of just copying it from the docs
	style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
	                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
	                       ('VALIGN',(0,0),(0,-1),'TOP'),
	                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
	                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
	                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
	                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
	                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
	                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
	                       ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
	                       ])
	

	#Configure style and word wrap
	s = getSampleStyleSheet()
	styleH = s['Bullet']
	stitle = s['Title']
	
	sdefinition = s['Definition']
	
	elements.append(Paragraph("Inventory document", stitle))
	elements.append(Spacer(1, 0.25 * inch))
	
	elements.append(Paragraph("Date: {}".format(strftime("%m/%d/%Y %H:%M")), styleH))
	elements.append(Spacer(1, 0.10 * inch))
	
	elements.append(Paragraph("Author: {}".format(request.user), styleH))
	elements.append(Spacer(1, 0.10 * inch))
	
	elements.append(Paragraph("Store: {}".format("Test storage & co."), styleH))
	elements.append(Spacer(1, 0.15 * inch))
	
	s = s["BodyText"]
	
	s.wordWrap = 'CJK'
	data2 = [[Paragraph(str(cell), s) for cell in row] for row in data]
	t=Table(data2)
	t.setStyle(style)
	
	#Send the data and build the file
	elements.append(t)
	
	totalprice = 0
	for p in Item.objects.all():
		totalprice+=(p.pojedinacnaCena*p.kolicina)
	
	elements.append(Spacer(1, 0.25 * inch))
	elements.append(Paragraph("Total items: {}".format(Item.objects.all().count()), sdefinition))
	
	elements.append(Spacer(1, 0.10 * inch))
	elements.append(Paragraph("Total value: {}".format(totalprice), sdefinition))
	
	doc.build(elements)
	
	return response







#add some special context here to show it on login page
def loginvisuals():
	
	return "Welcome to Storage application"

#add some special context here, to show it on main page
@login_required(login_url="/")	
def visual(request):
	graph_dict = {
					"graph":{
							"canvas1":{
										"labels" : ["January","February","March","April","May","June","July"],
										"datasets" : [
												{
													"label": "My First dataset",
													"fillColor" : "rgba(120,120,120,0.2)",
													"strokeColor" : "rgba(120,120,120,1)",
													"pointColor" : "rgba(120,120,120,1)",
													"pointStrokeColor" : "#fff",
													"pointHighlightFill" : "#fff",
													"pointHighlightStroke" : "rgba(120,120,120,1)",
													"data" : [65, 59, 80, 81, 56, 55, 40]
												}
											]
										},
							"canvas2":{
										"labels" : ["January2","February2","March2","April2","May2","June2","July2"],
										"datasets" : [
												{
													"label": "My Second dataset",
													"fillColor" : "rgba(120,120,120,0.2)",
													"strokeColor" : "rgba(120,120,120,1)",
													"pointColor" : "rgba(120,120,120,1)",
													"pointStrokeColor" : "#fff",
													"pointHighlightFill" : "#fff",
													"pointHighlightStroke" : "rgba(120,120,120,1)",
													"data" : [75, 49, 90, 71, 46, 65, 20]
												}
											]
										}
				 			},
				 	"left":{
				 			"elem1":{
				 						"title":["Naslov","www.google.com"],
				 						"description":"Bla bla",
				 					},
				 			"elem2":{
				 						"title":["Rat i mir","www.google.com"],
				 						"description":"Nek ide zivot",
				 					}
				 			},
				 	"centar":{
				 			"elem1":{
				 						"title":["Dummy","www.google.com"],
				 						"description":"Hello world",
				 					}
				 			},
				 	"right":{
				 			"elem1":{
				 						"title":["Hello","www.google.com"],
				 						"description":"world",
				 					}
				 			}
				 			
					}
	
	
	return HttpResponse(json.dumps(graph_dict), content_type="application/json")
