
function tripleToRGB(triple, opacity) {
  if (opacity) {
    return 'rgb(' + triple[0] + ', ' +
                    triple[1] + ', ' +
                    triple[2] + ', ' +
                    opacity + ')';
  }
  return 'rgb(' + triple[0] + ', ' +
                  triple[1] + ', ' +
                  triple[2] + ')';
}

function colorBrightness(triple) {
  return triple[0] + triple[1] + triple[2];
}

function compareBrightness(a, b) {
  return colorBrightness(a) - colorBrightness(b);
}

$(document).ready(function(){
        var colorThief = new ColorThief();
	var $img = $('#image');
        $img[0].crossOrigin = "Anonymous";

	$img.on('load', function(){
		var height = $img.height();
		
		//var padding = Math.floor(Math.random() * (15));
		//img.css({'padding': padding + 'px'});

                var palette = colorThief.getPalette($img[0], 16)

                var sortedPalette = palette.sort(compareBrightness);

                var titleColor = sortedPalette[0];
                var titleBackgroundColor = sortedPalette[sortedPalette.length - 1];

                var bookBackgroundColor = sortedPalette[0];
                var authorColor = sortedPalette[14];

                if (1 || Math.random() < 0.5) {
                  titleBackgroundColor = bookBackgroundColor;
                  titleColor = authorColor;
                  titleColor = sortedPalette[12];
                }

                //titleColor = [0, 255, 0];
	
		$('#title').css({'color': tripleToRGB(titleColor)});
		$('#title').css({'background-color': tripleToRGB(titleBackgroundColor)});

		$('#book').css({'background-color': tripleToRGB(bookBackgroundColor)});

		$('#author').css({'color': tripleToRGB(authorColor)});
		
		if (height > 550) {
			var less = height - 100;
			$('#title').css({'position': 'relative', 'top': '-' + less + 'px'});
			$('#title').css({'background-color': '#ffffff'});
			var opacity = (Math.random() * (1.0 - 0.50) + 0.50).toFixed(4);
                        var opacity = 255;
			$('#title').css({'background-color': 'rgba(255,255,255,' + opacity + ')'});

                        $('#title').css({'color': tripleToRGB(titleColor)});
                        $('#title').css({'background-color': tripleToRGB(titleBackgroundColor, opacity)});
			
			var border_thickness = Math.floor(Math.random() * (5));
			var border_radius = Math.floor(Math.random() * (12));

			var opacity_border = (Math.random() * (1.0 - 0.10) + 0.10).toFixed(4);
			$('#title').css({'border-radius': border_radius + 'px'});
			$('#title').css({'box-shadow': '0px 0px 0px ' + border_thickness + 'px rgba(0,0,0,' + opacity_border + ')'});
			
			$('#author').css({'position': 'relative', 'top': '-' + (less - 100) + 'px'});
			//$('#author').css({'background-color': '#ffffff'});
			//('#author').css({'background-color': 'rgba(255,255,255,' + opacity + ')'});

			$('#book').css({'height': height + 14});
		} else {
			var border_radius = Math.floor(Math.random() * (12));

			$('#title').css({'border-radius': border_radius + 'px'});
			
					var img_border_radius = Math.floor(Math.random() * (4));
		
		if (img_border_radius == 1) {
			$img.addClass('img-rounded');
		}
		if (img_border_radius == 2) {
			$img.addClass('img-polaroid');
		}
		if (img_border_radius == 3) {
			$img.addClass('img-circle');
		}
			
		}
		
                /*
		var div_height = $('#book').height();
		if (div_height < 450) {
			$('#book').css({'height': 450});
		} 
                */
		
	  
	  $("#book").toggle();

                console.log('height');
                console.log($('#title').height());
                console.log($('#title').outerHeight());
                console.log($('#title').innerHeight());
		if ($('#title').height() > 75) {
                        console.log('GOT BIG HEIGHT!!!!!!!!!!!!');
			$('#title').css({'font-size': '40px'});
			if ($('#title').height() > 75) {
                              console.log('Another BIG HEIGHT!!!!!!!!!!!!');
				$('#title').css({'font-size': '30px'});
			}
		}
		if ($('#title').offsetWidth < $('#title').scrollWidth) {
			$('#title').css({'font-size': '50px'});
		}
	});

	
});
