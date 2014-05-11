import pico
from ebaysdk.finding import Connection as finding
#from ebaysdk import finding


#filters = []
#filters.append({'name': 'LocatedIn','value': 'GB'})
#filters.append({'name': 'MinPrice','value': '2000'})
#filters.append({'name': 'MaxPrice','value': '23000'})
#filters.append({'name': 'HideDuplicateItems','value': 'true'})

sort_order = 'PricePlusShippingHighest'
filters_s = []


def get_from_ebay():	
	try:
		api = finding(siteid='EBAY-GB', appid="TomaszDo-ac84-4764-9f1f-c3d9de2f3e59") #prod server
		#api = finding(domain='svcs.sandbox.ebay.com', appid="TomaszDo-10f2-4c33-a762-9d5056c2784a")
		api.execute('findItemsAdvanced', { 'keywords': 'Car',
                                                   'categoryId' : [ '9801' , '29751' , '9800' ],
                                                  'itemFilter': filters_s , 'sortOrder': sort_order, })
		return api.response_dict()
	except Exception, e:
		raise e


def show_results(min_price=1000, max_price=5000):
#def show_results():
        global filters_s 
        filters_s = []
        filters_s.append({'name': 'LocatedIn','value': 'GB'})
        filters_s.append({'name': 'MinPrice','value': str(min_price) })
        filters_s.append({'name': 'MaxPrice','value': str(max_price) })
        filters_s.append({'name': 'HideDuplicateItems','value': 'true'})
		
        print filters_s
		
        x = get_from_ebay()

        print type(x)

        success = x['ack']['value']
        print success
        print '\n\n\n\n\n\n'

        f = x.items()

        results = x['searchResult']['item']

        count = 3
        output = []
        for i in results:

                output.append(i)
                count -= 1
                if not count:
                        break
        print x['itemSearchURL']['value']
        return output


def read_first():
	print "read"
	return "to expensive"
