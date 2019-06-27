import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, SemanticRolesOptions, SyntaxOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    #Autenticação do meu server no cloud
    iam_apikey='rA-eX7MNEepZZ8Vi1gz463UVp2aOm10WQFRYCQtfdehJ')

response = natural_language_understanding.analyze(
	#O Texto que tu quer Submeter
    text= 'Hey Doris, can you pick an coke for me ?', 
    #Todas as Features que eu quero usar
    features=Features(
        entities=EntitiesOptions(emotion=False, sentiment=False, limit=2),
        keywords=KeywordsOptions(emotion=False, sentiment=False, limit=2),
        semantic_roles=SemanticRolesOptions(keywords=True, 	entities=True, limit=2),
        syntax=SyntaxOptions())).get_result()

print(json.dumps(response, indent=2))