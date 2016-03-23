<!--[if HTML5]><![endif]-->
<!DOCTYPE html>
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]><html class="ie ie6 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en-us"> <![endif]-->
<!--[if IE 7]><html class="ie ie7 ie-lte9 ie-lte8 ie-lte7 no-js" lang="en-us"> <![endif]-->
<!--[if IE 8]><html class="ie ie8 ie-lte9 ie-lte8 no-js" lang="en-us"> <![endif]-->
<!--[if IE 9]><html class="ie9 ie-lte9 no-js" lang="en-us"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--> <html class="no-js" lang="en-us"> <!--<![endif]-->
<head>
<title>Example web scraping website</title>
  <!--[if !HTML5]>
      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <![endif]-->
  <!-- www.phpied.com/conditional-comments-block-downloads/ -->
  <!-- Always force latest IE rendering engine
       (even in intranet) & Chrome Frame
       Remove this if you use the .htaccess -->
	   
  <meta charset="utf-8" />

  <!-- http://dev.w3.org/html5/markup/meta.name.html -->
  <meta name="application-name" content="places" />

  <!--  Mobile Viewport Fix
        j.mp/mobileviewport & davidbcalhoun.com/2010/viewport-metatag
        device-width: Occupy full width of the screen in its current orientation
        initial-scale = 1.0 retains dimensions instead of zooming out if page height > device height
        user-scalable = yes allows the user to zoom in -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <link rel="shortcut icon" href="/places/static/images/favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="/places/static/images/favicon.png">

  <!-- All JavaScript at the bottom, except for Modernizr which enables
       HTML5 elements & feature detects -->
  <script src="/places/static/js/modernizr.custom.js"></script>

  <!-- include stylesheets -->
  

  <script type="text/javascript"><!--
    // These variables are used by the web2py_ajax_init function in web2py_ajax.js (which is loaded below).
    var w2p_ajax_confirm_message = "Are you sure you want to delete this object?";
    var w2p_ajax_disable_with_message = "Working...";
    var w2p_ajax_date_format = "%Y-%m-%d";
    var w2p_ajax_datetime_format = "%Y-%m-%d %H:%M:%S";
    var ajax_error_500 = 'An error occured, please <a href="/">reload</a> the page'
    //--></script>

<meta name="keywords" content="web2py, python, web scraping" />
<meta name="generator" content="Web2py Web Framework" />
<meta name="author" content="Richard Penman" />
<script src="/places/static/js/jquery.js" type="text/javascript"></script><link href="/places/static/css/calendar.css" rel="stylesheet" type="text/css" /><script src="/places/static/js/calendar.js" type="text/javascript"></script><script src="/places/static/js/web2py.js" type="text/javascript"></script><link href="/places/static/css/web2py.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/style.css" rel="stylesheet" type="text/css" /><link href="/places/static/css/web2py_bootstrap.css" rel="stylesheet" type="text/css" />


  

  <!-- uncomment here to load jquery-ui
       <link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/themes/ui-lightness/jquery-ui.css" type="text/css" media="all" />
       <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js" type="text/javascript"></script>
       uncomment to load jquery-ui //-->
  <noscript><link href="/places/static/css/web2py_bootstrap_nojs.css" rel="stylesheet" type="text/css" /></noscript>
  
</head>

<body>
  <!-- Navbar ================================================== -->
  <div class="navbar navbar-inverse">
    <div class="flash"></div>
    <div class="navbar-inner">
      <div class="container">
        
        <!-- the next tag is necessary for bootstrap menus, do not remove -->
        <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse" style="display:none;">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        
        <ul id="navbar" class="nav pull-right"><li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#" rel="nofollow">Log In</a><ul class="dropdown-menu"><li><a href="/user/register?_next=/" rel="nofollow"><i class="icon icon-user glyphicon glyphicon-user"></i> Sign Up</a></li><li class="divider"></li><li><a href="/user/login?_next=/" rel="nofollow"><i class="icon icon-off glyphicon glyphicon-off"></i> Log In</a></li></ul></li></ul>
        <div class="nav">
          
          <ul class="nav"><li class="web2py-menu-first"><a href="/">Home</a></li><li class="web2py-menu-last"><a href="/search">Search</a></li></ul>
          
        </div><!--/.nav-collapse -->
      </div>
    </div>
  </div><!--/top navbar -->

  <div class="container">
    <!-- Masthead ================================================== -->
      
    <header class="mastheader row" id="header">
        <div class="span12">
            <div class="page-header">
                <h1>
                    Example web scraping website
                    <small></small>
                </h1>
            </div>
        </div>
    </header>
	

    <section id="main" class="main row">
        

        <div class="span12">
            
            

<div id="results">
<table><tr><td><div><a href="/view/Afghanistan-1"><img src="/places/static/images/flags/af.png" /> Afghanistan</a></div></td><td><div><a href="/view/Aland-Islands-2"><img src="/places/static/images/flags/ax.png" /> Aland Islands</a></div></td></tr><tr><td><div><a href="/view/Albania-3"><img src="/places/static/images/flags/al.png" /> Albania</a></div></td><td><div><a href="/view/Algeria-4"><img src="/places/static/images/flags/dz.png" /> Algeria</a></div></td></tr><tr><td><div><a href="/view/American-Samoa-5"><img src="/places/static/images/flags/as.png" /> American Samoa</a></div></td><td><div><a href="/view/Andorra-6"><img src="/places/static/images/flags/ad.png" /> Andorra</a></div></td></tr><tr><td><div><a href="/view/Angola-7"><img src="/places/static/images/flags/ao.png" /> Angola</a></div></td><td><div><a href="/view/Anguilla-8"><img src="/places/static/images/flags/ai.png" /> Anguilla</a></div></td></tr><tr><td><div><a href="/view/Antarctica-9"><img src="/places/static/images/flags/aq.png" /> Antarctica</a></div></td><td><div><a href="/view/Antigua-and-Barbuda-10"><img src="/places/static/images/flags/ag.png" /> Antigua and Barbuda</a></div></td></tr></table>
</div>

<div id="pagination">

    &lt; Previous

|

    <a href="/index/1">Next &gt;</a>

</div>

            
        </div>

        
    </section><!--/main-->

    <!-- Footer ================================================== -->
    <div class="row">
        <footer class="footer span12" id="footer">
        </footer>
    </div>

  </div> <!-- /container -->

  <!-- The javascript =============================================
       (Placed at the end of the document so the pages load faster) -->
  <script src="/places/static/js/bootstrap.min.js"></script>
  <script src="/places/static/js/web2py_bootstrap.js"></script>
  <!--[if lt IE 7 ]>
      <script src="/places/static/js/dd_belatedpng.js"></script>
      <script> DD_belatedPNG.fix('img, .png_bg'); //fix any <img> or .png_bg background-images </script>
      <![endif]-->
</body>
</html>

