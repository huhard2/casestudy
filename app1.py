import subprocess, sys
from flask import Flask, jsonify

def add_bridge(bridge):
	test0 = subprocess.call(['sudo', 'ovs-vsctl', 'add-br', bridge])

def show_bridge():
	test1 = subprocess.check_output(['sudo','ovs-vsctl', 'show'])
	return test1

def del_br(bridge):
	test2 = subprocess.call(['sudo','ovs-vsctl','del-br', bridge])

def update_bridge(bridge, options):
        subprocess.call(['sudo', 'ovs-vsctl', 'set', 'Bridge', bridge, options])

def add_interface(bridge,interface):
	test3 = subprocess.call(['sudo','ovs-vsctl','add-port', bridge, interface])

def add_vlan(bridge,interface,tag):
	test4 = subprocess.call(['sudo','ovs-vsctl','add-port',bridge, interface, tag])

def del_vlan(interface):
	test5 = subprocess.call(['sudo','ovs-vsctl','del-port', interface])

def update_vlan(interface,tag):
	test6 = subprocess.call(['sudo','ovs-vsctl','set','port',interface, tag])

def show_vlan():
	test7 = subprocess.call(['sudo','ovs-vsctl','show'])
	return test7

def show_trunk():
	test12 = subprocess.call(['sudo','ovs-vsctl','show'])
	return test12

def add_trunk(interface,trunk):
	test13 = subprocess.call(['sudo','ovs-vsctl','set','port', interface, trunk])

def update_trunk(interface,trunk):
	test14 = subprocess.call(['sudo','ovs-vsctl','set','port', interface, trunk])

def del_trunk(interface):
        test15 = subprocess.call(['sudo','ovs-vsctl','del-port', interface])

def add_vxlan(interface,vxlan):
	test9 = subprocess.call(['sudo', 'ovs-vsctl','add-port', interface, vxlan])

def add_route(ip_preflix,bridge,gateway):
	test8 = subprocess.call(['sudo','ovs-appctl','ovs/route/add', ip_preflix , bridge , gateway ])

def show_route():
	test10 = subprocess.call(['sudo','ovs-appctl','ovs/route/show'])
	return test10

def del_route(ip_preflix):
	test11 = subprocess.call(['sudo','ovs-appctl' ,'ovs/route/del' , ip_preflix])

