def message_creator(text):
   response = {
      'computadora' : 'Con mi computadora puedo programar usando Python',
      'celular' : 'En mi celular puedo aprender usando la app de Platzi',
      'cable' : '¡Hay un cable en mi bota!',
      'ornitorrinco' : 'Artículo no encontrado'
   }
   # Escribe tu solución 👇

   '''result = text in response
   if result:
      result = response[text]
   else:
      result = "Artículo no encontrado"'''
   
   result = "Artículo no encontrado"
   if text in response.keys():
      result = response[text]
      

   return result

text = 'ornitorrinco'
response = message_creator(text)
print(response)