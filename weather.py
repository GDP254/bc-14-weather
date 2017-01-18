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


def RequestOpenWeather(code):
	conn = httplib.HTTPConnection("api.openweathermap.org", 80)
	conn.request("GET", "/data/2.5/weather?id=%d&appid=071be05bfba2c97dd5e60e061664c889" % code)
	resp = conn.getresponse()
	click.echo('Request State: %d - %s' % (resp.status, resp.reason))
	data = json.loads(resp.read().decode("UTF-8"))
	if resp.status == 200:
		click.echo("\n	Description: "+data['weather'][0]['description']+"\n	Temperature: "+str(data['main']['temp'])+" Kelvin")
	else:
		click.echo(data)


def ShowProvinces():
	click.echo("\n The following are the currently available Kenyan provinces: \n")
	for i in locations.keys():
		click.echo('	'+i)

def CleanInput(inp):
	if type(inp) is str or type(inp) is unicode:
		inp = inp.strip()
		inp = inp.lower()
		inp = inp.title()
		if inp in locations:
			#to do
			click.echo("Incoming Information ....")
			RequestOpenWeather(locations[inp])
			#click.echo(info)
		else:
			click.echo("\nPlease try again providing your selected province as specified")
	else:
		click.echo("\nPlease try again providing your selected province as specified")


@click.option('--province', prompt="\nPlease enter the province you would like the weather for (e.g. central) :",
              help='The province in Kenya you would like to know the weather for.')
@click.command(ShowProvinces())
def  KenyanWeather(province):
    """Simple program that request weather information based on select provinces in Kenya."""
    CleanInput(province)

if __name__ == '__main__':
    KenyanWeather()