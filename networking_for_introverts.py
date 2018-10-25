import httplib
import urllib
import json
import datetime
import time
import webbrowser


def get_instagram(latitude, longitude, distance, min_timestamp, max_timestamp, access_token):
    get_request = '/v1/media/search?lat=' + latitude
    get_request += '&lng=' + longitude
    get_request += '&distance=' + distance
    get_request += '&min_timestamp=' + str(min_timestamp)
    get_request += '&max_timestamp=' + str(max_timestamp)
    get_request += '&access_token=' + access_token
    # get_request += '&scope=basic+public_content+follower_list+comments+relationships+likes'
    local_connect = httplib.HTTPSConnection('api.instagram.com', 443)
    local_connect.request('GET', get_request)
    return local_connect.getresponse().read()


def get_vk(location_latitude, location_longitude, distance, min_timestamp, max_timestamp):
    get_request = '/method/photos.search?lat=' + location_latitude
    get_request += '&long=' + location_longitude
    get_request += '&count=100'
    get_request += '&radius=' + distance
    get_request += '&start_time=' + str(min_timestamp)
    get_request += '&end_time=' + str(max_timestamp)
    local_connect = httplib.HTTPSConnection('api.vk.com', 443)
    local_connect.request('GET', get_request)
    print(get_request)
    return local_connect.getresponse().read()


def timestamptodate(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S') + ' UTC'


def parse_instagram(location_latitude, location_longitude, distance, min_timestamp, max_timestamp, date_increment,
                    access_token):
    print 'Starting parse instagram..'
    print 'GEO:', location_latitude, location_longitude
    print 'TIME: from', timestamptodate(min_timestamp), 'to', timestamptodate(max_timestamp)
    file_inst = open('instagram_' + location_latitude + location_longitude + '.html', 'w')
    file_inst.write('<html>')
    local_min_timestamp = min_timestamp
    while True:
        if (local_min_timestamp >= max_timestamp):
            break
        local_max_timestamp = local_min_timestamp + date_increment
        if (local_max_timestamp > max_timestamp):
            local_max_timestamp = max_timestamp
        print timestamptodate(local_min_timestamp), '-', timestamptodate(local_max_timestamp)
        local_buffer = get_instagram(location_latitude, location_longitude, distance, local_min_timestamp,
                                     local_max_timestamp, access_token)
        instagram_json = json.loads(local_buffer)
        for local_i in instagram_json['data']:
            file_inst.write('<br>')
            file_inst.write('<img src=' + local_i['images']['standard_resolution']['url'] + '><br>')
            file_inst.write(timestamptodate(int(local_i['created_time'])) + '<br>')
            file_inst.write(local_i['link'] + '<br>')
            file_inst.write('<br>')
        local_min_timestamp = local_max_timestamp
    file_inst.write('</html>')
    file_inst.close()


def parse_vk(location_latitude, location_longitude, distance, min_timestamp, max_timestamp, date_increment):
    print 'Starting parse vkontakte..'
    print 'GEO:', location_latitude, location_longitude
    print 'TIME: from', timestamptodate(min_timestamp), 'to', timestamptodate(max_timestamp)
    # print 'TIME: from', timestamptodate(min_timestamp), 'to', timestamptodate(max_timestamp)

    report_file = 'vk_' + location_latitude + '_' + location_longitude + '_' + start_search + '_' + end_search + '.html'
    with open(report_file, 'w') as file_inst:
        file_inst.write('<html>')
        local_min_timestamp = min_timestamp

        while True:
            if local_min_timestamp >= max_timestamp:
                break
            local_max_timestamp = local_min_timestamp + date_increment
            if local_max_timestamp > max_timestamp:
                local_max_timestamp = max_timestamp
            print timestamptodate(local_min_timestamp), '-', timestamptodate(local_max_timestamp)
            vk_json = json.loads(
                get_vk(location_latitude, location_longitude, distance, local_min_timestamp, local_max_timestamp))
            for local_i in vk_json['response']:
                if type(local_i) is int:
                    continue
                file_inst.write('<br>')
                file_inst.write('<img src=' + local_i['src_big'] + '><br>')
                file_inst.write(timestamptodate(int(local_i['created'])) + '<br>')
                user_link = 'http://vk.com/id' + str(local_i['owner_id'])
                file_inst.write('<a href="' + user_link + '">' + user_link + '</a>' + '<br>')
                file_inst.write('<br>')
            local_min_timestamp = local_max_timestamp
        file_inst.write('</html>')

    webbrowser.open(report_file)


def date_to_timestamp(date_str):
    tmp_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    return time.mktime(tmp_date.timetuple())


if __name__ == '__main__':
    # lat = 55.740701
    # lon = 37.609161

    lat = '59.939243'
    lon = '30.315561'

    location_latitude = str(lat)
    location_longitude = str(lon)

    # location_latitude = '51.535142'
    # location_longitude = '-0.195696'
    distance = '100'

    start_search = "YYYY-MM-D HH:MM"
    end_search = "YYYY-MM-D HH:MM"

    min_timestamp = date_to_timestamp(start_search)
    max_timestamp = date_to_timestamp(end_search)
    date_increment = 60 * 60 * t  # every t hours

    # parse_instagram(location_latitude, location_longitude, distance, min_timestamp, max_timestamp, date_increment,
    #                 instagram_access_token)
    parse_vk(location_latitude, location_longitude, distance, min_timestamp, max_timestamp, date_increment)
