function fireShutter() {
	$('#cam_img').on('click', function() {
		$('#window_fade').css("display", "inherit");
		$("cam_img img").css("display", "none");
		var shutter_speed = $('#shutter_speed').val();
		var white_balance = $('#white_balance').val();

		var dataString = "shutter_speed=" + shutter_speed + "&white_balance=" + white_balance;

		$.ajax({
			url: $SCRIPT_ROOT + "/shutter",
			data: dataString,
			success: function(data) {
				function change_attr(data, callback) {
					$('#cam_img img').attr("src", $SCRIPT_ROOT + "/static/images/" + data);
					setTimeout(function() {
						callback();
					}, 500);
				}

				change_attr(data, function() {
					$('cam_img img').css("display", "block");
					$('#window_fade').css("display", "none");
				});
			}
		});
	});
}


fireShutter();