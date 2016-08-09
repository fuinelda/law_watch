function toJson(stringtojson){
	return stringtojson.replace(/&#39;/g,'"').replace(/\r\n/g,'\<br \/\>');
}
