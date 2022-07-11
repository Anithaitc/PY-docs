export.handler = function(event,context,callback){
callback(null,"some success message:");
return{
"statuCode":200,
"message":"This is the first NodeJS Lambda"
}
}: