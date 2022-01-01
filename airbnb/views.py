from django.views.generic import View
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.
# Creating a view for searching autocomplete here

class SearchView(View):
	def get(self, request, *args, **kwargs):
		# this was basic api
		# now lets imlement autocomplete api
		query = self.kwargs['query']
		r = requests.get(f"https://www.airbnb.co.in/api/v2/autocompletes?country=IN&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&language=en&locale=en-IN&num_results=5&user_input={query}&api_version=1.2.0&satori_config_token=EhIiQhIiIjISEjISIRISIlJCNS4VBhVgFQKFAgA&vertical_refinement=homes&region=-1&options=should_filter_by_vertical_refinement%7Chide_nav_results%7Cshould_show_stays%7Csimple_search%7Cflex_destinations_june_2021_launch_web_treatment")
		# Done now we need to parse json and structure it according to our requirements
		suggestions = dict(r.json())
		suggestions = suggestions['autocomplete_terms']
		respnonse = {"results":[]}
		for s in suggestions:
			respnonse['results'].append(s['display_name'])
		return JsonResponse(respnonse, safe=False)
