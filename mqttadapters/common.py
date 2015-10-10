def add_mqtt_arguments(parser):
    parser.add_argument('-H', '--host', type=str, dest='host',
                        default='localhost', help='hostname of MQTT')
    parser.add_argument('-p', '--port', type=int, dest='port', default=1883,
                        help='port of MQTT')
    parser.add_argument('-u', '--username', type=str, dest='username',
                        default=None, help='username for the broker')
    parser.add_argument('-P', '--password', type=str, dest='password',
                        default=None, help='password for the broker')
                        
def connect_mqtt(args, client):
    if args.username is not None:
        client.username_pw_set(args.username, args.password)
    client.connect(args.host, args.port)