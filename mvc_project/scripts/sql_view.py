sql_query = '''SELECT "ajax_api_ip_address"."id", "ajax_api_ip_address"."ip_address",
 "ajax_api_ip_address"."eth0", "ajax_api_ip_address"."host",
 "ajax_api_ip_address"."sap_id" FROM "ajax_api_ip_address" '''

view_query = '''CREATE VIEW  [OR REPLACE] IP_Address_View AS SELECT "ajax_api_ip_address"."id", "ajax_api_ip_address"."ip_address",
 "ajax_api_ip_address"."eth0", "ajax_api_ip_address"."host",
 "ajax_api_ip_address"."sap_id" FROM "ajax_api_ip_address '''
