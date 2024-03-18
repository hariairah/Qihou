import discord

color = 0xFF6500
key_features = {
    'temp' : 'Temperature (in °C)',
    'feels_like' : 'Feels Like (in °C)',
    'temp_min' : 'Minimum Temperature (in °C)',
    'temp_max' : 'Maximum Temperature (in °C)'
}

def parse_data(data):
    del data['humidity']
    del data['pressure']
    return data

def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather in {location}.',
        color=color
    )
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=False
        )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
