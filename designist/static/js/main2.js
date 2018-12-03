var $menu = $('#menu');
    $body = $('body'),
	$menu.wrapInner('<div class="inner"></div>');
	$menu._locked = false;
	$menu._lock = function() {
		if ($menu._locked)
			return false;
		$menu._locked = true;
		window.setTimeout(function() {
			$menu._locked = false;
		}, 350);
		return true;
	};
	$menu._show = function() {
		if ($menu._lock())
			$body.addClass('is-menu-visible');
	};
	$menu._hide = function() {
		if ($menu._lock())
			$body.removeClass('is-menu-visible');
	};
	$menu._toggle = function() {
		if ($menu._lock())
			$body.toggleClass('is-menu-visible');
	};
	$menu
		.appendTo($body)
		.on('click', function(event) {
			event.stopPropagation();
		})
		.on('click', 'a', function(event) {
			var href = $(this).attr('href');
			event.preventDefault();
			event.stopPropagation();
			// Hide.
				$menu._hide();
			// Redirect.
				if (href == '#menu')
					return;
				window.setTimeout(function() {
					window.location.href = href;
				}, 350);
		})
		.append('<a class="close" href="#menu">Close</a>');
	$body
		.on('click', 'a[href="#menu"]', function(event) {
			event.stopPropagation();
			event.preventDefault();
			// Toggle.
				$menu._toggle();
		})
		.on('click', function(event) {
			// Hide.
				$menu._hide();
		})
		.on('keydown', function(event) {
			// Hide on escape.
				if (event.keyCode == 27)
					$menu._hide();
		});
    
    /*goto top*/
	var goToTop = function() {

		$('.js-gotop').on('click', function(event){
			
			event.preventDefault();

			$('html, body').animate({
				scrollTop: $('html').offset().top
			}, 500, 'easeInOutExpo');
			
			return false;
		});

		$(window).scroll(function(){

			var $win = $(window);
			if ($win.scrollTop() > 200) {
				$('.js-top').addClass('active');
			} else {
				$('.js-top').removeClass('active');
			}

		});
	
	};
function dian(ogj, url, typename){
	// 点赞\踩
	var id      = $(ogj).find('a').attr("data-id");
	var num     = parseInt($('#like_count').text());
	var zanlist = $.cookie(typename);
	var flag    = -1;
	if (zanlist != null) {
		flag = zanlist.indexOf(id + ',');
	}
	if (flag < 0) {
		$.ajax({
			type: "Post",
			url: url,
			data: {id:id, field:'praise'},
			dataType: "json",
			error: function(){
			},
			success : function(data){
				if(data.status){
				    $('#like_count').text(num + 1);
					//点赞成功
					if(zanlist == null){
						zanlist = id + ',';
					}else{
						zanlist = zanlist + id + ',';
					}
					$.cookie(typename, zanlist);
				}
			}
		});
	} else {
		alert('亲，你已经点过赞咯!');
	}
}
