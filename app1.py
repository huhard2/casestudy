import subprocess, sys
from flask import Flask, jsonify

"""
@auth.get_password
def get_password(username):
	if username == 'joey':
		return 'ang'
	return None

	@auth.error_handler
	def unauthorised():
		return make_response(jsonify( {'error': 'Unauthorised access' } ),

	@cs.error_handler(400)
	def not_found(error):
		return make_response(jsonify { 'error' : 'Bad Request' } ), 400):
	
	@cs.errorhandler(404)
	def not_found(error):
		return make_response(jsonify {'error' : 'Not Found' } ),404)
"""
def add_bridge(bridge):
	test0 = subprocess.call(['sudo', 'ovs-vsctl', 'add-br', bridge])

def show_bridge():
	test1 = subprocess.check_output(['sudo','ovs-vsctl', 'show'])
	return test1

def del_br(bridge):
	test2 = subprocess.call(['sudo','ovs-vsctl','del-br', bridge])

def add_interface(bridge,interface):
	test3 = subprocess.call(['sudo','ovs-vsctl','add-port', bridge, interface])

def add_vlan(bridge,interface,tag):
	test4 = subprocess.call(['sudo','ovs-vsctl','add-port',bridge, interface, tag])

def del_vlan(interface):
	test5 = subprocess.call(['sudo','ovs-vsctl','del-port', interface])

def update_vlan(interface,tag):
	test6 = subprocess.call(['sudo','ovs-vsctl','set','port',interface, tag])


