<!DOCTYPE html>
<html lang="en">
<head>
        <!-- Mercurial head: a123e58 -->
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="google-site-verification" content="m41-YA2o4kXb32RmyuClA1zAXZCyaGaDEUj1QIc5bmc" />
        <title>dpaste: DUL2WG3W2</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <link rel="icon" type="image/x-icon" href="https://dpaste.b-cdn.net/static/pastebin/favicon.ico">
        <link rel="icon" type="image/png" sizes="32x32" href="https://dpaste.b-cdn.net/static/pastebin/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="https://dpaste.b-cdn.net/static/pastebin/favicon-16x16.png">
        <link rel="apple-touch-icon" sizes="180x180" href="https://dpaste.b-cdn.net/static/pastebin/apple-touch-icon.png">
        <link rel="manifest" href="https://dpaste.b-cdn.net/static/pastebin/site.webmanifest">

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script defer src="https://media.ethicalads.io/media/client/ethicalads.min.js"></script>

        
<script defer src="https://cdn.jsdelivr.net/npm/shareon@1/dist/shareon.min.js" type="text/javascript"></script>
<link href="https://cdn.jsdelivr.net/npm/shareon@1/dist/shareon.min.css" rel="stylesheet">
<script>
    function key(event, letter) {
        return (event.charCode == letter.charCodeAt() || event.charCode == letter.charCodeAt() + 32)
        }
    function subview_redirect(path_end) {
        // Drop line anchor and/or syntax-override extension for proper base
        location.href = location.pathname.split('#')[0].split('.')[0] + path_end;
        }
    function indicate_wrap() { $("#softwrap_toggle").text("UNWRAP"); location.hash = "wrap"; }
    function indicate_unwrap() { $("#softwrap_toggle").text("SOFT WRAP"); location.hash = ""; }
    function softwrap_toggle() {
        $("pre").toggleClass("softwrap");
        $(".linenodiv").toggle();
        if ($("#softwrap_toggle").text() == "SOFT WRAP") { indicate_wrap(); }
        else { indicate_unwrap(); }
        }
    function toggle_star() {
        $.ajax({type:"POST", url:"/api/v2/star/DUL2WG3W2"});
        if ($("#toggle_star").html() == "☆") { $("#toggle_star").html("&starf;") }
        else { $("#toggle_star").html("&star;") }
        }
    function mark_linked_line() {
        $('.linemark').remove();
        $('a[href="'+location.hash+'"]').after('<svg height="10" width="16" class="linemark"> <polygon points="3,0 15,4 3,9" style="fill:#99f"></svg>');
        }
    function copy_to_clipboard() {
        if (!navigator.clipboard) {
            console.log("Clipboard API not available")
            return
        }
        try {
            navigator.clipboard.writeText($('#raw-content').html())
            $('#copy-success').show()
        } catch (err) {
            console.error('Copying raw content failed: ', err)
        }

    }
    $(document).ready(function() {
        window.onhashchange = mark_linked_line
        if (location.hash == "#wrap") { softwrap_toggle(); indicate_wrap(); }
        if (location.hash.indexOf("#line-") === 0) { mark_linked_line(); }
        $("#softwrap_toggle").click(softwrap_toggle);
        $("#toggle_star").click(toggle_star);
        $('#copy-button').click(copy_to_clipboard)
    });
    $(document).keypress(function(event){
        if (key(event, 'W')) { softwrap_toggle(); }
         // For pastes only, not diffs
            if (key(event, 'C')) { copy_to_clipboard() }
            if (key(event, 'D')) { subview_redirect('/duplicate/') }
            if (key(event, 'R')) { subview_redirect('.txt') }
            if (key(event, '*')) { toggle_star() }
            
        
        
        });
    
    $(document).keyup(function(event){
        if (event.keyCode == 8 || event.keyCode == 46) { subview_redirect('/delete/'); }
        });
</script>


        <link rel="stylesheet" href="https://dpaste.b-cdn.net/static/pastebin/css/normalize.css">
        <link rel="stylesheet" href="https://dpaste.b-cdn.net/static/pastebin/css/skeleton.css">
        <link rel="stylesheet" href="https://dpaste.b-cdn.net/static/pastebin/css/main.css">
        <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;700&amp;display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Fira+Mono" rel="stylesheet">

        <style>
            
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: #ffffcc }
.highlight { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    .linenos { padding-right: 0 }
    .softwrap { white-space: pre-wrap; }
    h1 i { color: #888;}
    td.code { padding-left: 0 }
    #copy-success { color: #fff; font-weight: bold }

        </style>
    </head>
    <body>
        <div id='container'>
        <div class="topbuttons">
            
                <a href="/accounts/login/" class="button"><b>Log in</b></a>
            
            <a href="/" title="Create a new paste" 
                class=" button">New</a>
            <a href="/api/v2/" title="Paste creation API"
                class="   button">API</a>
            <a href="/help" title="Usage tips"
                class="  button">Help</a>
            <a href="/about" title="Colophon, backstory, stats, tweets"
                class=" button">About</a>
        </div>
        


<h1></h1>
<div class="row">
    
    
    
585 bytes of <strong>Plain text</strong><br>
Created 15 seconds ago


    &mdash; expires in <strong>7 days</strong>

<span style="display:none"><br>https://dpaste.com/DUL2WG3W2</span>

</div>
<div class="row actionbuttons">

<a id="copy-button" title="Copy raw content (shortcut: 'C'">COPY TO CLIPBOARD<span id="copy-success" hidden>&nbsp;&#10004;</span></a>
<a id="softwrap_toggle" title="Toggle visual wrap of long lines (shortcut: 'W')">SOFT WRAP</a>
<a href="/DUL2WG3W2.txt" title="Plaintext version (shortcut: 'R')">RAW TEXT</a>

<a href="/DUL2WG3W2/duplicate/" title="Make a new paste based on this one (shortcut: 'D')">DUPLICATE</a>
<a href="/DUL2WG3W2/diff" title="Diff this paste against another one">DIFF</a>

</div>

<table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><span class="normal"><a href="#line-1">1</a></span>
<span class="normal"><a href="#line-2">2</a></span>
<span class="normal"><a href="#line-3">3</a></span>
<span class="normal"><a href="#line-4">4</a></span>
<span class="normal"><a href="#line-5">5</a></span>
<span class="normal"><a href="#line-6">6</a></span>
<span class="normal"><a href="#line-7">7</a></span>
<span class="normal"><a href="#line-8">8</a></span>
<span class="normal"><a href="#line-9">9</a></span></pre></div></td><td class="code"><div class="highlight"><pre><span></span><a id="line-1" name="line-1"></a>try:
<a id="line-2" name="line-2"></a>    wiki_res = wikipedia.summary(parameter, sentences=2)
<a id="line-3" name="line-3"></a>    if &quot;Джордж Перри Флойд&quot; not in wiki_res: message(wikipedia.summary(parameter) + &quot;\nПодробнее: &quot; + ShortUrl(wikipedia.page(parameter).url), reply=True)
<a id="line-4" name="line-4"></a>    else: message(&quot;Аъаъаъаъааъъаъаа убили негра убили негра убили негра\nПодробнее: &quot; + ShortUrl(wikipedia.page(parameter).url), reply=True)
<a id="line-5" name="line-5"></a>except wikipedia.exceptions.DisambiguationError as e:
<a id="line-6" name="line-6"></a>    mr = &#39;\n&#39;.join(str(e).split(&#39;\n&#39;)[1:])
<a id="line-7" name="line-7"></a>    message(f&quot;Уточните, что вы имели ввиду:\n {mr}&quot;, reply=True)
<a id="line-8" name="line-8"></a>except Exception as e:
<a id="line-9" name="line-9"></a>    message(&#39;Ничего не найдено. &#39;)
</pre></div>
</td></tr></table>

<div id="raw-content" hidden>
try:
    wiki_res = wikipedia.summary(parameter, sentences=2)
    if &quot;Джордж Перри Флойд&quot; not in wiki_res: message(wikipedia.summary(parameter) + &quot;\nПодробнее: &quot; + ShortUrl(wikipedia.page(parameter).url), reply=True)
    else: message(&quot;Аъаъаъаъааъъаъаа убили негра убили негра убили негра\nПодробнее: &quot; + ShortUrl(wikipedia.page(parameter).url), reply=True)
except wikipedia.exceptions.DisambiguationError as e:
    mr = &#x27;\n&#x27;.join(str(e).split(&#x27;\n&#x27;)[1:])
    message(f&quot;Уточните, что вы имели ввиду:\n {mr}&quot;, reply=True)
except Exception as e:
    message(&#x27;Ничего не найдено. &#x27;)
</div>

<hr>

<div class="shareon">
    <p>Share:</p>
    <button class="mastodon"></button>
    <button class="reddit"></button>
    <button class="twitter"></button>
</div>


        </div> 

        
        <script>
            window.fwSettings={'widget_id':22000000180 };
            !function(){if("function"!=typeof window.FreshworksWidget){var n=function(){n.q.push(arguments)};n.q=[],window.FreshworksWidget=n}}();
        </script>
        <script defer src='https://widget.freshworks.com/widgets/22000000180.js'></script>
    </body>
</html>