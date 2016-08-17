window.onload = function(){
	var tabs = document.getElementsByClassName('insidetab');
	for(i in tabs){
		if(tabs[i].style){
			tabs[i].style.width = (100 / tabs[i].attributes.value.value - 2) + '%';
		}
	}
}

function toJson(stringtojson){
	return stringtojson.replace(/&#39;/g,'"').replace(/\r\n/g,'\<br \/\>');
}

function showtab(tabtn,idname){
	var tabs = document.getElementsByClassName('tabbtn');
	for(i in tabs){
		if(tabs[i].style){
			tabs[i].style.background = '';
			tabs[i].style.color = 'black';
			tabs[i].style.fontWeight = 'normal';
		}
	}
	tabtn.style.background = 'gray';
	tabtn.style.color = 'white';
	tabtn.style.fontWeight = 'bold';
	console.log(tabtn.style.fontWeight);
	tabs = document.getElementsByClassName('tabcontent');
	for(i in tabs){
		if(tabs[i].style){
			tabs[i].style.display = 'none';
		}
	}
	document.getElementById(idname).style.display = 'block';
}
