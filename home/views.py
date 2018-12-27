from home.models import People
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db.models import Count
import json
from django.core import serializers
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def first_fetch(request):
    return render(request, 'home/index.html')

def pie_data(request):
    dataset_pie = People.objects.values('sex').annotate(total=Count('sex')).order_by('sex')
    chart_pie = {
        'chart': {
        'renderTo': 'container_chartPie',
        'plotBackgroundColor': 'white',
        'plotBorderWidth': '0',
        'plotShadow': 'true',
        'type': 'pie'
    },
    'title': {
        'text': 'Distribution of number of males and females'
    },
    'tooltip': {
        'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    'plotOptions': {
        'pie': {
            'allowPointSelect': 'true',
            'cursor': 'pointer',
            'dataLabels': {
                'enabled': 'false',
                'format': '<b>{point.name}</b>',
                'style': {
                    'color': '(Highcharts.theme && Highcharts.theme.contrastTextColor) || black'
                },
                'connectorColor': 'red',
            },
            'showInLegend': 'true'
        }
    },
        'series': [{
            'name': 'Share',
            'colorByPoint': 'true',
            'data': list(map(lambda row: {'name': row['sex'], 'y': row['total']}, dataset_pie))
        }]
    }
    return JsonResponse(chart_pie)


def bar_data(request):
    dataset_bar = People.objects.values('relationship').annotate(total=Count('relationship')).order_by('relationship')
    chart_bar = {
	    'chart': {
	    	'renderTo': 'container_bar',
	    	'plotBackgroundColor': 'white',
        	'plotBorderWidth': '0',
        	'plotShadow': 'true',
	        'type': 'column'
	    },
	    'title': {
	        'text': 'Number of People in each relationship'
	    },
	    'xAxis': {
	        'type': 'category',
	        'labels': {
	            'rotation': -45,
	            'style': {
	                'fontSize': '13px',
	                'fontFamily': 'Verdana, sans-serif'
	            }
	        }
	    },
	    'yAxis': {
	        'min': 0,
	        'title': {
	            'text': 'Population'
	        }
	    },
	    'legend': {
	        'enabled': 'false'
	    },
	    'tooltip': {
	        'pointFormat': 'People in this relationship: <b>{point.y:.1f}</b>'
	    },
	    'series': [{
	        'name': 'Population',
	        'data': list(map(lambda row: [row['relationship'], row['total']], dataset_bar)),
	        'dataLabels': {
	            'enabled': 'true',
	            'rotation': -90,
	            'color': '#FFFFFF',
	            'align': 'right',
	            'format': '{point.y:.1f}',
	            'y': 10,
	            'style': {
	                'fontSize': '13px',
	                'fontFamily': 'Verdana, sans-serif'
	            }
	        }
	    }]
	}
    return JsonResponse(chart_bar)


def display_data(request):
	sex =None
	race = None
	relationship = None

	data = People.objects.all().order_by('item_id')

	if any(v is not None for v in [request.GET.get('sex'), request.GET.get('race'), request.GET.get('relationship')]):
		if request.GET.get('sex') is not "":
			data = data.filter(sex=request.GET.get('sex'))
		if request.GET.get('race') is not "":
			data = data.filter(race=request.GET.get('race'))
		if request.GET.get('relationship') is not "":
			data = data.filter(relationship=request.GET.get('relationship'))

	page = request.GET.get('page')

	results_per_page = 100
	paginator = Paginator(data, results_per_page)
	try:
		data = paginator.get_page(page)
	except PageNotAnInteger:
		data = paginator.get_page(1)
	except EmptyPage:
		data = paginator.get_page(paginator.num_pages)

	output_data = {
		'data': data,
		'title': "List"
	}	
	return render(request, 'home/display.html', {'data': data})
