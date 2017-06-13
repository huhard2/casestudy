#!flask/bin/python
import subprocess
import app1
from flask import Flask, jsonify
import json
from flask import request

call = Flask(__name__)

@call.route('/addbr', methods=['POST'])
def addbr():
	bridge = request.json ['bridge']
	app1.add_bridge(bridge)
	return jsonify({'bridge name' : bridge}), 201

@call.route('/listbr', methods=['GET'])
def showbr():
	return app1.show_bridge()

@call.route('/delbr/<bridge>', methods=['DELETE'])
def delbr(bridge):
	app1.del_br(bridge)
	return jsonify({'Bridge Deleted' : bridge}), 201

@call.route('/addinterface', methods=['POST'])
def addport():
	bridge = request.json['bridge']
	interface = request.json['interface']
	app1.add_interface(bridge,interface)
	return jsonify({'bridge' : bridge,
			'interface' : interface}),201

@call.route('/addvlan', methods=['POST'])
def addvlan():
	bridge = request.json['bridge']
	interface = request.json['interface']
	tag = request.json['tag']
	app1.add_vlan(bridge,interface,tag)
	return jsonify ({'bridge' : bridge,
			'interface' : interface,
			'tag' : tag}), 201

@call.route('/delvlan/<interface>', methods=['DELETE'])
def delvlan(interface):
	app1.del_vlan(interface)
	return jsonify({'VLAN Deleted' : interface}),201

@call.route('/updatevlan/<interface>', methods=['PUT'])
def updatevlan(interface):
	tag = request.json['tag']
	app1.update_vlan(interface, tag)
	return jsonify({'VLAN Updated' : interface ,
			'tag' : tag}), 201


if __name__ == '__main__':
	call.run(debug=True)
