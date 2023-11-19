import requests
from ncclient import manager
import xml.dom.minidom
m = manager.connect(
 host="192.168.8.128",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False
 )
netconf_hostname = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <hostname>CSR_local_1</hostname>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
netconf_loopback = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>1</name>
 <description>Test Loopback address</description>
 <ip>
 <address>
 <primary>
 <address>10.1.1.1</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
netconf_GigabitEthernet = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <name>GigabitEthernet1</name>
 <description>Main GagabitEthernet port</description>
 <ip>
 <address>
 <primary>
 <address></address>
 <mask></mask>
 </primary>
 </address>
 </ip>
 </interface>
</native>
</config>
"""

access_token = 'ZjE0NGRlNWMtY2ZkYy00ZDAwLWJmZjgtOGQ0MjJkZTA3MzZhNWJiOGI3YzItMGI4_P0A1_36820416-bfff-433a-84bf-39585b2b3f67'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNjE3NzQzMjAtODcwYi0xMWVlLWE5M2MtZmYyODEzOTM2NjQ1'
message = 'The CSR Router has had an update to the configs'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())

access_token = 'ZjE0NGRlNWMtY2ZkYy00ZDAwLWJmZjgtOGQ0MjJkZTA3MzZhNWJiOGI3YzItMGI4_P0A1_36820416-bfff-433a-84bf-39585b2b3f67'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOGQ3MDQ4MDAtODcwYi0xMWVlLThkMzktNjkwODA0MjMzNDE1'
message = 'The CSR Router has had an update to the configs'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())