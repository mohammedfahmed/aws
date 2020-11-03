import boto3

TableName = "emane"
columns=["Age","First", "Last"]

client = boto3.client('dynamodb')

DB = boto3.resource('dynamodb')
table = DB.Table(TableName)

PrimaryColumn = 'nodeid'
PrimaryKey = 1
response = table.get_item(Key={PrimaryColumn:PrimaryKey})

PrimaryKey = 5
response = table.put_item(Item={PrimaryColumn:PrimaryKey,  columns[0]: 44, columns[1] :"Youtube",  columns[2]: "Python" })

PrimaryKey = 5 
response = table.delete_item( Key={ PrimaryColumn: PrimaryKey } ) 

response = client.describe_table(TableName = TableName)

from boto3.dynamodb.conditions import Key
response = table.query(KeyConditionExpression=Key('nodeid').eq(0))


from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('emane')

response = table.scan(FilterExpression=Attr('nodeid').gte(0))


from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('emane')

response = table.scan(FilterExpression=Attr('Age').gte(28))
