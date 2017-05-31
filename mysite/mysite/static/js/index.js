// Typewriter.js
// https://github.com/ronv/Typewriter.js

var aText = new Array(
  "<span class='terminal__text__span'>hi, i'm parker truesdell</span>",
  "<span class='terminal__text__span'>a full stack software developer</span>", 
  "<span class='terminal__text__span'>living in santa clara, california</span>",
  "<span class='terminal__text__span'>i drink a lot of coffee</span>",
  "<span class='terminal__text__span'>and build beautiful websites</span>",
  "<span class='terminal__text__span'># # # # # # # # # # # # # # # # # #</span>",
  "<span class='terminal__text__span'>see my <a href='/portfolio/'>portfolio</a> or profile on <a href='https://github.com/ptruesdell'>github</a></span>",
  "<span class='terminal__text__span'>and</span>",
  "<span class='terminal__text__span'>read my <a href='/blog/'>blog</a></span>"
);
var iSpeed = 15; 
var iIndex = 0; 
var iArrLength = aText[0].length; 
var iScrollAt = 10; 
 
var iTextPos = 0; 
var sContents = ''; 
var iRow; 
 
function typewriter()
{
 sContents =  ' ';
 iRow = Math.max(0, iIndex-iScrollAt);
 var destination = document.getElementById("typedtext");
 
 while ( iRow < iIndex ) {
  sContents += aText[iRow++] + '<br />';
 }
 destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "_";
 if ( iTextPos++ == iArrLength ) {
  iTextPos = 0;
  iIndex++;
  if ( iIndex != aText.length ) {
   iArrLength = aText[iIndex].length;
   setTimeout("typewriter()", 200);
  }
 } else {
  setTimeout("typewriter()", iSpeed);
 }
}

$(function() {
	$( ".terminal" ).draggable();
});