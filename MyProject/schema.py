import email
from http import client
from random import choices
from unittest.util import _MAX_LENGTH
import graphene
from graphene_django import DjangoObjectType
from myclient.models import STATUS_CHOICES, Client, Contract


class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = '__all__'
        
        
        
class ContractType(DjangoObjectType):
    class Meta:
        model = Contract
        fields = '__all__'
            

class Query(graphene.ObjectType):
        client = graphene.Field(ClientType, id=graphene.Int())
        all_clients = graphene.List(ClientType)
        contract = graphene.Field(ContractType, id=graphene.Int())
        all_contracts = graphene.List(ContractType)
        total_clients = graphene.Int()
        total_contracts = graphene.Int()
        contract_description = graphene.String()   
         

      
        
        def resolve_client_address(self, info, **kwargs):
            return Client.objects.all().values_list('address', flat=True)
        
        def resolve_contract_description(self, info, **kwargs):
            description = kwargs.get('description')
            if description is not None:
                return Contract.objects.filter(contract_description=description)

        def resolve_all_clients(self, info, **kwargs):
            return Client.objects.all()

        def resolve_client(self, info, **kwargs):
            id = kwargs.get('id')
            if id is not None:
                return Client.objects.get(pk=id)

        def resolve_all_contracts(self, info, **kwargs):
            return Contract.objects.all()

        def resolve_contract(self, info, **kwargs):
            id = kwargs.get('id')
            if id is not None:
                return Contract.objects.get(pk=id)
        # customers = graphene.List(CustomerType)
        contracts = graphene.List(ContractType)

        def resolve_clients(self, info):
            return Client.objects.all()

        def resolve_contracts(self, info):
            return Contract.objects.all() 
        
        def resolve_total_clients(self, info):
            return Client.objects.count()
        def resolve_total_contracts(self, info):
            return Contract.objects.count()
        
        
class CreateClient(graphene.Mutation):
    client = graphene.Field(ClientType)
    class Arguments:
        id = graphene.ID()
        name = graphene.String()   
        phone = graphene.String()
        email = graphene.String()
        address = graphene.String()
        date_created = graphene.Date()
        

    def mutate(self, info, name, phone, email, address, id,  date_created):
        client = Client(name=name, id=id, phone=phone, email=email, address=address,  date_created=date_created)
        client.save()

        return CreateClient(client=client)
 
        
class CreateContract(graphene.Mutation):
    contract = graphene.Field(ContractType)
    class Arguments:
        contract_name = graphene.String()    
        contract_type = graphene.String()
        contract_status = graphene.String()
        contract_description = graphene.String()
        date_created = graphene.Date()
        id = graphene.ID()
        

    def mutate(self, info, contract_name, id, contract_type, contract_status, contract_description, date_created):
        contract = Contract(contract_name=contract_name, id=id, contract_type=contract_type, contract_status=contract_status, contract_description=contract_description, date_created=date_created)
        contract.save()
        
class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
    create_contract = CreateContract.Field()
    

      
        
schema = graphene.Schema(query=Query, mutation=Mutation)



