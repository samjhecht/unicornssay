from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):

		html = """<html><head></head><body>
							<pre>

							  ________________________   \
							 &lt; Unicorns are the best! &gt;   \
							  ------------------------     \\
							                     \          \\
							                      \          &gt;\/7
							                             _.-(6'  \
							                            (=___._/` \
							                                 )  \ |
							                                /   / |
							                               /    &gt; /
							                              j    &lt; _\
							                          _.-' :      ``.
							                          \ r=._\        `.
							                         &lt;`\\_  \         .`-.
							                          \ r-7  `-. ._  ' .  `\
							                           \`,      `-.`7  7)   )
							                            \/         \|  \'  / `-._
							                                      ||    .'
							                                       \\  (
							                                        &gt;\  &gt;
							                                     ,.-' &gt;.'
							                                    &lt;.'_.''
							                                      &lt;'
							</pre>
							
							</body></html>"""

    return HttpResponse(html)
