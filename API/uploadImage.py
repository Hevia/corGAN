#!flask/bin/python
from flask import Flask, jsonify
import base64
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.documents as documents
import azure.cosmos.errors as errors

config = {
    'ENDPOINT': 'https://corgan-cosmos.documents.azure.com:443/',
    'PRIMARYKEY': 'REMOVEDKEY',
    'DATABASE': 'Corgi_Images',
    'CONTAINER': 'Generated_Images'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                    'masterKey': config['PRIMARYKEY']})
database_link = 'dbs/' + config['DATABASE']

# Pending Deletion
# database = client.ReadDatabase(database_link)
# databases = list(client.QueryDatabases({"query": "SELECT * FROM CosmosContainer"}))
# for p in databases: print (p)
# if len(databases) > 0:
#	print('Database with id \'{0}\' was found'.format(id))
# else:
#	print('No database with id \'{0}\' was found'. format(id))

# Convert Image to Base64 then upload
with open("corgo.jpg", "rb") as f:
	encodedZip = base64.b64encode(f.read())
	# print(encodedZip)

collection_link = database_link + '/colls/' + config['CONTAINER']
container = client.ReadContainer(collection_link)

item1 = client.CreateItem(container['_self'], {
	'id': 'TestImage6',
	'base64': encodedZip.decode()
	}
)