# File: request_fields.py
#
# Copyright (c) 2016-2018 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
req_part_base = {
   "config": {
       "limit": "",
       "timeRange": "CUSTOM",
       "customStart": "",
       "customEnd": "",
       "order": [
         {
           "direction": "ASCENDING",
           "field": {"name": "FirstTime"}
         }
       ],
       "fields": []
   }
}


common_fields = [{u'name': u'FirstTime'}]

alarm_fields_list = [
    {u'name': u'AlarmAcknowledgeDate'},
    {u'name': u'AlarmAcknowledgedByUserID'},
    {u'name': u'AlarmAssigneeUserID'},
    {u'name': u'AlarmSeverity'},
    {u'name': u'AlarmStatus'},
    {u'name': u'AlarmTriggerDate'}
]

event_fields_list = [
    {u'name': u'Access_Mask'},
    {u'name': u'Access_Privileges'},
    {u'name': u'Access_Resource'},
    {u'name': u'Action.Name'},
    {u'name': u'Agent_GUID'},
    {u'name': u'Action'},
    {u'name': u'ASNGeoDst'},
    {u'name': u'DstMac'},
    {u'name': u'DstPort'},
    {u'name': u'ZoneDst'},
    {u'name': u'NDDevIDDst'},
    {u'name': u'NDDevIDSrc'},
    {u'name': u'DSID'},
    {u'name': u'DSIDSigID'},
    {u'name': u'WriteTime'},
    {u'name': u'EventCount'},
    {u'name': u'Flow'},
    {u'name': u'ID'},
    {u'name': u'NDDevIFDst'},
    {u'name': u'NDDevIFSrc'},
    {u'name': u'AlertID'},
    {u'name': u'IPSID'},
    {u'name': u'LastTime'},
    {u'name': u'Rule.NormID'},
    {u'name': u'Protocol'},
    {u'name': u'Reviewed'},
    {u'name': u'Severity'},
    {u'name': u'SigID'},
    {u'name': u'ASNGeoSrc'},
    {u'name': u'SrcIP'},
    {u'name': u'SrcMac'},
    {u'name': u'SrcPort'},
    {u'name': u'ZoneSrc'},
    {u'name': u'VLan'},
    {u'name': u'Analyzer_DAT_Version'},
    {u'name': u'App_Layer_Protocol'},
    {u'name': u'AppID'},
    {u'name': u'Application_Protocol'},
    {u'name': u'Area'},
    {u'name': u'Users.Name'},
    {u'name': u'Attacker_IP'},
    {u'name': u'Attribute_Type'},
    {u'name': u'Authentication_Type'},
    {u'name': u'Authoritative_Answer'},
    {u'name': u'AvgSeverity'},
    {u'name': u'Bcc'},
    {u'name': u'Bytes_from_Client'},
    {u'name': u'Bytes_from_Server'},
    {u'name': u'Bytes_Received'},
    {u'name': u'Bytes_Sent'},
    {u'name': u'Caller_Process'},
    {u'name': u'Catalog_Name'},
    {u'name': u'Category'},
    {u'name': u'Cc'},
    {u'name': u'Client_Version'},
    {u'name': u'CnC_Host'},
    {u'name': u'CommandID'},
    {u'name': u'Confidence'},
    {u'name': u'Contact_Name'},
    {u'name': u'Contact_Nickname'},
    {u'name': u'Cookie'},
    {u'name': u'Count'},
    {u'name': u'Creator_Name'},
    {u'name': u'DAT_Version'},
    {u'name': u'Database_GUID'},
    {u'name': u'Database_ID'},
    {u'name': u'Database_Name'},
    {u'name': u'Datacenter_ID'},
    {u'name': u'Datacenter_Name'},
    {u'name': u'DB2_Plan_Name'},
    {u'name': u'Delivery_ID'},
    {u'name': u'Description'},
    {u'name': u'NDDeviceInterface_NDDevIFDst.Name'},
    {u'name': u'NDDevice_NDDevIDDst.ManagementIP'},
    {u'name': u'NDDevice_NDDevIDDst.SystemName'},
    {u'name': u'GUIDDst'},
    {u'name': u'DstIP'},
    {u'name': u'Zone_ZoneDst.Name'},
    {u'name': u'Destination_Directory'},
    {u'name': u'Destination_Filename'},
    {u'name': u'Destination_Hostname'},
    {u'name': u'Destination_Logon_ID'},
    {u'name': u'Destination_Network'},
    {u'name': u'Destination_UserID'},
    {u'name': u'Destination_Zone'},
    {u'name': u'Detection_Method'},
    {u'name': u'Device_Action'},
    {u'name': u'Device_IP'},
    {u'name': u'Device_Port'},
    {u'name': u'Device_URL'},
    {u'name': u'Direction'},
    {u'name': u'Directory'},
    {u'name': u'DNS - Class'},
    {u'name': u'DNS - Class_Name'},
    {u'name': u'DNS - Query'},
    {u'name': u'DNS - Response_Code'},
    {u'name': u'DNS - Response_Code_Name'},
    {u'name': u'DNS - Type'},
    {u'name': u'DNS - Type_Name'},
    {u'name': u'DNS_Class'},
    {u'name': u'DNS_Name'},
    {u'name': u'DNS_Server_IP'},
    {u'name': u'DNS_Type'},
    {u'name': u'DomainID'},
    {u'name': u'GeoLoc_ASNGeoDst.Msg'},
    {u'name': u'GeoLoc_ASNGeoDst.Latitude'},
    {u'name': u'GeoLoc_ASNGeoDst.Longitude'},
    {u'name': u'GeoLoc_ASNGeoDst.XCoord'},
    {u'name': u'GeoLoc_ASNGeoDst.YCoord'},
    {u'name': u'Elapsed_Time'},
    {u'name': u'End_Page'},
    {u'name': u'Engine_List'},
    {u'name': u'Sequence'},
    {u'name': u'SessionID'},
    {u'name': u'Trusted'},
    {u'name': u'Event_Class'},
    {u'name': u'External_Application'},
    {u'name': u'External_DB2_Server'},
    {u'name': u'External_Device_ID'},
    {u'name': u'External_Device_Name'},
    {u'name': u'External_Device_Type'},
    {u'name': u'External_EventID'},
    {u'name': u'External_Hostname'},
    {u'name': u'External_SessionID'},
    {u'name': u'External_SubEventID'},
    {u'name': u'Facility'},
    {u'name': u'File_Hash'},
    {u'name': u'File_ID'},
    {u'name': u'File_Operation'},
    {u'name': u'File_Operation_Succeeded'},
    {u'name': u'File_Path'},
    {u'name': u'File_Size'},
    {u'name': u'File_Type'},
    {u'name': u'Filename'},
    {u'name': u'FlowID'},
    {u'name': u'From'},
    {u'name': u'From_Address'},
    {u'name': u'FTP_Command'},
    {u'name': u'Grid_Master_IP'},
    {u'name': u'Group_Name'},
    {u'name': u'Handheld_ID'},
    {u'name': u'Handle_ID'},
    {u'name': u'Hash'},
    {u'name': u'Hash_Type'},
    {u'name': u'Hops'},
    {u'name': u'HostID'},
    {u'name': u'Incident_ID'},
    {u'name': u'Virtual_Machine_ID'},
    {u'name': u'Virtual_Machine_Name'},
    {u'name': u'Volume_ID'},
    {u'name': u'VPN_Feature_Name'},
    {u'name': u'Vulnerability_References'},
    {u'name': u'Web_Domain'},
    {u'name': u'Wireless_SSID'},
    {u'name': u'FirstTime'},
    {u'name': u'Incoming_ID'},
    {u'name': u'Instance_GUID'},
    {u'name': u'Interface'},
    {u'name': u'NDIFIDDst'},
    {u'name': u'NDIFIDSrc'},
    {u'name': u'Interface_Dest'},
    {u'name': u'IPS.Name'},
    {u'name': u'Job_Name'},
    {u'name': u'Job_Type'},
    {u'name': u'Language'},
    {u'name': u'LastTime_usec'},
    {u'name': u'Local_User_Name'},
    {u'name': u'Logical_Unit_Name'},
    {u'name': u'Logon_Type'},
    {u'name': u'LPAR_DB2_Subsystem'},
    {u'name': u'Mail_ID'},
    {u'name': u'Mailbox'},
    {u'name': u'Mainframe_Job_Name'},
    {u'name': u'Malware_Insp_Action'},
    {u'name': u'Malware_Insp_Result'},
    {u'name': u'Management_Server'},
    {u'name': u'Message_ID'},
    {u'name': u'Message_Text'},
    {u'name': u'Method'},
    {u'name': u'NAT_Details'},
    {u'name': u'New_Reputation - ATD_File'},
    {u'name': u'New_Reputation - GTI_Cert'},
    {u'name': u'New_Reputation - GTI_File'},
    {u'name': u'New_Reputation - TIE_Cert'},
    {u'name': u'New_Reputation - TIE_File'},
    {u'name': u'New_Value'},
    {u'name': u'Rule_NDSNormSigID.msg'},
    {u'name': u'NTP_Client_Mode'},
    {u'name': u'NTP_Offset_To_Monitor'},
    {u'name': u'NTP_Opcode'},
    {u'name': u'NTP_Request'},
    {u'name': u'NTP_Server_Mode'},
    {u'name': u'Num_Copies'},
    {u'name': u'Object_GUID'},
    {u'name': u'Object_Type'},
    {u'name': u'ObjectID'},
    {u'name': u'Old_Reputation - ATD_File'},
    {u'name': u'Old_Reputation - GTI_Cert'},
    {u'name': u'Old_Reputation - GTI_File'},
    {u'name': u'Old_Reputation - TIE_Cert'},
    {u'name': u'Old_Reputation - TIE_File'},
    {u'name': u'Old_Value'},
    {u'name': u'Operating_System'},
    {u'name': u'Organizational_Unit'},
    {u'name': u'Parent_File_Hash'},
    {u'name': u'PCAP_Name'},
    {u'name': u'PID'},
    {u'name': u'Policy_ID'},
    {u'name': u'Policy_Name'},
    {u'name': u'Priority'},
    {u'name': u'Privileged_User'},
    {u'name': u'Privileges'},
    {u'name': u'Process_Name'},
    {u'name': u'Query_Response'},
    {u'name': u'Queue_ID'},
    {u'name': u'Reason'},
    {u'name': u'Recipient_Count'},
    {u'name': u'Recipient_ID'},
    {u'name': u'Referer'},
    {u'name': u'Registry - Key'},
    {u'name': u'Registry - Value'},
    {u'name': u'Registry_Key'},
    {u'name': u'Registry_Value'},
    {u'name': u'RemCaseID'},
    {u'name': u'RemOpenTicketTime'},
    {u'name': u'Reputation'},
    {u'name': u'Reputation_Name'},
    {u'name': u'Reputation_Score'},
    {u'name': u'Reputation_Server_IP'},
    {u'name': u'Request_Type'},
    {u'name': u'Response_Code'},
    {u'name': u'Response_Time'},
    {u'name': u'Return_Code'},
    {u'name': u'RTMP_Application'},
    {u'name': u'Rule.ID'},
    {u'name': u'Rule.msg'},
    {u'name': u'Rule_Name'},
    {u'name': u'Search_Query'},
    {u'name': u'Security_ID'},
    {u'name': u'Sensor_Name'},
    {u'name': u'Sensor_Type'},
    {u'name': u'Sensor_UUID'},
    {u'name': u'Server_ID'},
    {u'name': u'Service_Name'},
    {u'name': u'Session_Status'},
    {u'name': u'SHA1'},
    {u'name': u'Share_Name'},
    {u'name': u'Signature_Name'},
    {u'name': u'SNMP_Error_Code'},
    {u'name': u'SNMP_Item'},
    {u'name': u'SNMP_Item_Type'},
    {u'name': u'SNMP_Operation'},
    {u'name': u'SNMP_Version'},
    {u'name': u'GUIDSrc'},
    {u'name': u'NDDeviceInterface_NDDevIFSrc.Name'},
    {u'name': u'NDDevice_NDDevIDSrc.ManagementIP'},
    {u'name': u'NDDevice_NDDevIDSrc.SystemName'},
    {u'name': u'Zone_ZoneSrc.Name'},
    {u'name': u'Source_Context'},
    {u'name': u'Source_Logon_ID'},
    {u'name': u'Source_Network'},
    {u'name': u'Source_UserID'},
    {u'name': u'Source_Zone'},
    {u'name': u'Spam_Score'},
    {u'name': u'SQL_Command'},
    {u'name': u'SQL_Statement'},
    {u'name': u'GeoLoc_ASNGeoSrc.Msg'},
    {u'name': u'GeoLoc_ASNGeoSrc.Latitude'},
    {u'name': u'GeoLoc_ASNGeoSrc.Longitude'},
    {u'name': u'GeoLoc_ASNGeoSrc.XCoord'},
    {u'name': u'GeoLoc_ASNGeoSrc.YCoord'},
    {u'name': u'Start_Page'},
    {u'name': u'Status'},
    {u'name': u'Step_Count'},
    {u'name': u'Step_Name'},
    {u'name': u'Sub_Status'},
    {u'name': u'Subcategory'},
    {u'name': u'Subject'},
    {u'name': u'SWF_URL'},
    {u'name': u'Table_Name'},
    {u'name': u'Target_Class'},
    {u'name': u'Target_Context'},
    {u'name': u'Target_Process_Name'},
    {u'name': u'TC_URL'},
    {u'name': u'ThirdPartyType.Name'},
    {u'name': u'Threat_Category'},
    {u'name': u'Threat_Handled'},
    {u'name': u'Threat_Name'},
    {u'name': u'To'},
    {u'name': u'To_Address'},
    {u'name': u'URL'},
    {u'name': u'URL_Category'},
    {u'name': u'AppIDCat'},
    {u'name': u'UserFld10Cat'},
    {u'name': u'CommandIDCat'},
    {u'name': u'UserFld21Cat'},
    {u'name': u'UserFld22Cat'},
    {u'name': u'UserFld23Cat'},
    {u'name': u'UserFld24Cat'},
    {u'name': u'UserFld25Cat'},
    {u'name': u'UserFld26Cat'},
    {u'name': u'UserFld27Cat'},
    {u'name': u'DomainIDCat'},
    {u'name': u'HostIDCat'},
    {u'name': u'ObjectIDCat'},
    {u'name': u'UserIDDstCat'},
    {u'name': u'UserIDSrcCat'},
    {u'name': u'UserFld8Cat'},
    {u'name': u'UserFld9Cat'},
    {u'name': u'User_Agent'},
    {u'name': u'User_Nickname'},
    {u'name': u'UserIDDst'},
    {u'name': u'UserIDSrc'},
    {u'name': u'UUID'},
    {u'name': u'Version'},
    {u'name': u'Victim_IP'}
]
