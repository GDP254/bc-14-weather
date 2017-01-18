import click, httplib, json

locations = {
	"Rift Valley": 400744,
	"Nyanza": 182763,
	"Coast" : 400740,
	"Western": 400743,
	"Central": 400742,
	"Nairobi": 184742,
	"Eastern": 400741,
	"North Eastern": 400745
}


def request_open_weather(code):
	print("Connecting ...")
	conn = httplib.HTTPConnection("api.openweathermap.org", 80)
	print("	Configuring request with necessary information")
	conn.request("GET", "/data/2.5/weather?id=%d&appid=071be05bfba2c97dd5e60e061664c889" % code)
	print("	Request sent and response retrieved")
	resp = conn.getresponse()
	click.echo('Request State: %d - %s' % (resp.status, resp.reason))
	print("	Extracting and formating data from response")
	data = json.loads(resp.read().decode("UTF-8"))
	print("	if request was succesful:")
	if resp.status == 200:
		print("		Closing connection.")
		conn.close()
		print("		Displaying information.")
		click.echo("\n	Description: "+data['weather'][0]['description']+"\n	Temperature: "+str(data['main']['temp'])+" Kelvin")
	else:
		print("		Closing connection.")
		conn.close()
		print("		Displaying raw data.")
		click.echo(data)


def show_provinces():
	click.echo("\n The following are the currently available Kenyan provinces: \n")
	for i in locations.keys():
		click.echo('	'+i)

def clean_input(inp):
	if type(inp) is str or type(inp) is unicode:
		inp = inp.strip()
		inp = inp.lower()
		inp = inp.title()
		if inp in locations:
			#to do
			click.echo("Incoming Information ....")
			request_open_weather(locations[inp])
			#click.echo(info)
		else:
			click.echo("\nPlease try again providing your selected province as specified")
	else:
		click.echo("\nPlease try again providing your selected province as specified")

#use click decorators to configure command line options
@click.option('--province', prompt="\nPlease enter the province you would like the weather for (e.g. central) :",
              help='The province in Kenya you would like to know the weather for.')
#declare KenyanWeather as a click command and specify ShowProvinces to run before this command
@click.command(show_provinces())
def  KenyanWeather(province):
    """Simple program that request weather information based on select provinces in Kenya."""
    clean_input(province)

if __name__ == '__main__':
    KenyanWeather()