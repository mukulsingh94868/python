import requests, json
import secret

def publish(net_name, jdata):
    url = secret.URL
    headers = {'content-type': 'application/json'}
    headers['API-KEY'] = secret.API_KEYS[net_name]
    payload = {'network': net_name}
    payload['data'] = jdata
    resp = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers)
    return resp.status_code

def radio_publish():
    # initialize “net” object
    …
    #
    while True:
        jdata = net.dump_state()
        try:
            resp = publish(net.name, jdata)
            time.sleep(net.step)
        except:
            break
        net.next()
    logger.debug('Last published data is > {}'.format(jdata))
    return jdata

