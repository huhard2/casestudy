#!flask/bin/python
import subprocess, json
import sub_joey
from flask import Flask, jsonify, request, abort, make_response
from flask.ext.httpauth import HTTPBasicAuth

call = Flask(__name__)

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
        if username == 'joey':
                return 'ang'
        return None

@auth.error_handler
def unauthorised():
        return make_response(jsonify( {'error': 'Unauthorised access' } ), 403)

@call.errorhandler(400)
def not_found(error):
        return make_response(jsonify( {'error' : 'Bad Request' } ), 400)
        
@call.errorhandler(404)
def not_found(error):
        return make_response(jsonify( {'error' : 'Not Found' } ),404)


@call.route('/addbr', methods=['POST'])
@auth.login_required
def addbr():
	bridge = request.json ['bridge']
	app1.add_bridge(bridge)
	return jsonify({'bridge name' : bridge}), 201

@call.route('/listbr', methods=['GET'])
@auth.login_required
def showbr():
	bridge = app1.show_bridge()
	return jsonify ({'bridge' : bridge.splitlines()})

@call.route('/delbr/<bridge>', methods=['DELETE'])
@auth.login_required
def delbr(bridge):
	app1.del_br(bridge)
	return jsonify({'Bridge Deleted' : bridge}), 201

@call.route('/updatebridge/<bridge>', methods=['PUT'])
@auth.login_required
def update_bridge(bridge):
        options = request.json['options']
        app1.update_bridge(bridge,options)
	return jsonify({'bridge': bridge,
			'options': options}), 201

@call.route('/addinterface', methods=['POST'])
@auth.login_required
def addport():
	bridge = request.json['bridge']
	interface = request.json['interface']
	app1.add_interface(bridge,interface)
	return jsonify({'bridge' : bridge,
			'interface' : interface}),201

@call.route('/addvlan', methods=['POST'])
@auth.login_required
def addvlan():
	bridge = request.json['bridge']
	interface = request.json['interface']
	tag = request.json['tag']
	app1.add_vlan(bridge,interface,tag)
	return jsonify ({'bridge' : bridge,
			'interface' : interface,
			'tag' : tag}), 201

@call.route('/delvlan/<interface>', methods=['DELETE'])
@auth.login_required
def delvlan(interface):
	app1.del_vlan(interface)
	return jsonify({'VLAN Deleted' : interface}),201

@call.route('/updatevlan/<interface>', methods=['PUT'])
@auth.login_required
def updatevlan(interface):
	tag = request.json['tag']
	app1.update_vlan(interface, tag)
	return jsonify({'VLAN Updated' : interface ,
			'tag' : tag}), 201

@call.route('/showvlan', methods=['GET'])
@auth.login_required
def showvlan():
        bridge = app1.show_bridge()
        return jsonify ({'bridge' : bridge.splitlines()})

@call.route('/showtrunk', methods=['GET'])
@auth.login_required
def showtrunk():
	bridge = app1.show_bridge()
	return jsonify ({'bridge' : bridge.splitlines()})

@call.route('/addtrunk', methods=['POST'])
@auth.login_required
def addtrunk():
        interface = request.json['interface']
        trunk = request.json['trunk']
        app1.add_trunk(interface,trunk)
        return jsonify ({'interface' : interface,
                        'trunk' : trunk}), 201

@call.route('/updatetrunk/<interface>', methods=['PUT'])
@auth.login_required
def updatetrunk(interface):
        trunk = request.json['trunk']
        app1.update_trunk(interface, trunk)
        return jsonify({'Trunk Updated' : interface ,
                        'trunk' : trunk}), 201

@call.route('/deltrunk/<interface>', methods=['DELETE'])
@auth.login_required
def deltrunk(interface):
        app1.del_trunk(interface)
        return jsonify({'Trunk Deleted' : interface}),201


@call.route('/addvxlan', methods=['GET'])
@auth.login_required
def addvxlan():
	interface = request.json['interface']
	vxlan = request.json['vxlan']
	app1.add_vxlan(interface,vxlan)
	return jsonify ({'interface' : interface,
			'vxlan' : vxlan}) ,201 

@call.route('/addroute', methods=['POST'])
@auth.login_required
def addroute():
	ip_preflix = request.json['ip_preflix']
        bridge = request.json['bridge']
        gateway = request.json['gateway']
        app1.add_route(ip_preflix,interface,gateway)
        return jsonify ({'ip_preflix' : ip_preflix,
			'bridge' : bridge,
                        'gateway' : gateway}), 201

@call.route('/showroute', methods=['GET'])
@auth.login_required
def showroute():
        route = app1.show_route()
        return jsonify ({'route' : route.splitlines()})

@call.route('/delroute/<ip_preflix>', methods=['DELETE'])
@auth.login_required
def delroute(ip_preflix):
        app1.del_route(ip_preflix)
        return jsonify({'IP Route Deleted' : interface}),201


if __name__ == '__main__':
	call.run(debug=True)
