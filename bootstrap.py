#!/usr/bin/env python3.3
# -*- coding: UTF-8 -*-
# enable debugging
import file_search


class BootsHeadsNFeet:
    """Creates 2 diffrent bootstrap headers
    one with the option of a "custom.css" (header) file
    the other with out (header_no_custome).
    (footer) creates the standard bootstrap footer 
    and point to jQuery file.
    """
    def __init__(self,title_is,footer_is):
        self.title_is=str(title_is)
        self.footer_is=str(footer_is)
    def header(self):
        html_header1 = """
        <!doctype html>
        <html>
        <title>"""
        html_header2 = """</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap  -->
        <head>
        <link href ="/bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link href="/bootstrap/css/custom.css" rel="stylesheet">
        <script src="/bootstrap/js/respond.js"></script>
        </head>
        <body>

        """
        print(html_header1)
        print(self.title_is)
        print(html_header2)
    def header_no_custom(self):
        html_header1 = """
        <!doctype html>
        <html>
        <title>"""
        html_header2 = """</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap  -->
        <head>
        <link href ="/bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <script src="/bootstrap/js/respond.js"></script>
        </head>
        <body>

        """
        print(html_header1)
        print(self.title_is)
        print(html_header2)
    def footer(self):
        foot_see1 = """
              <div class="footer">
        <p>"""
        
        foot_see2 = """</p>
              </div>
            </div> <!-- /container -->
            <!-- javascript -->
            <script src="http://code.jquery.com/jquery-latest.min.js"></script>
            <script src="/bootstrap/js/bootstrap.min.js"></script>
          </body>
        </html>
        """
        print(foot_see1)
        print(self.footer_is)
        print(foot_see2)

class Container:
    """Creates a container div for start and end of the page"""
    def __init__(self):
        self = self
    def make_container(self):
        print('<div class="container">')
    def end_container(self):
        print('</div> <!-- for Container-->')

class MakeDivRows:
    """Makes div with row classes, as well as columns that can have adjustable numbers,
    the last 2 arguments are for droping in wells and thumbnails"""    
    def __init__(self,cols_len,col_size,rowstyle='',colstyle=''):
        self.col_size=col_size
        self.cols_len=cols_len
        self.rowstyle=rowstyle
        self.colstyle=colstyle
    def row_start(self):
        if self.rowstyle == '' and self.colstyle =='':
            """first argument is the col size i.e.'md'/'lg'
            second argument is the col lenght '6'/'12'
            If a thrid argument if stated 
            will add a style to the row div (defaults to none).
            A forth argument will
            add a style to the row class (defaults to none)         
            """
            print('<div class="row">')
            print('<div class="col-'+self.col_size+'-'+self.cols_len+'">')
        elif self.rowstyle != '' and self.colstyle =='':
            print('<div class="row '+self.rowstyle+'">')
            print('<div class="col-'+self.col_size+'-'+self.cols_len+'">')
        elif self.rowstyle != '' and self.colstyle !='':
            print('<div class="row '+self.rowstyle+'">')
            print('<div class="col-'+self.col_size+'-'+self.cols_len+' '+self.colstyle+'">')       
    def col_start(self):
        if self.colstyle =='':
            print('<div class="col-'+self.col_size+'-'+self.cols_len+'">')
        else:
            print('<div class="col-'+self.col_size+'-'+self.cols_len+' '+self.colstyle+'">')          
    def col_end(self):
        """creates an end div for col div and matching
        commented out html htlm tag"""
        print('</div> <!-- for col-->') 
    def row_end(self):
        """creates an end div for col then row div and matching
        commented out html htlm tag"""
        print('</div> <!-- for col-->')
        print('</div> <!-- for row-->')
        
class NavBar:
    """takes a dictionary and returns a nav bar with no drop downs
        dictionary must be writen this way dict_links{"LINK NAME":'somelink.py'}"""
    def __init__(self,link_is):
        self.link_is = link_is
    def build_navbar(self):
        navheader="""<div class="container">
        <div class="row">
        <nav class="navbar navbar-default navbar-fixed-top navbar-inverse">
        <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        </button>
        </div>
        <div class="collapse navbar-collapse" id="collapse">
        <ul class="nav navbar-nav"> """
        print(navheader)
        for ln,ahref in self.link_is.items():
            print("<li><a href='"+ahref+"'>"+ln+"</a></li>")
        print('</ul>')
        print('</ul>')
        print('</div>')
        print('</nav>')
        print('</div>')
            
class JumboTron:
    """Creates 2 difrent types of jumbotrons
    see method documentation for more info."""
    def __init__(self,text,heading="",h='1'):
        self.text=str(text)
        self.heading=str(heading)
        self.h=str(h)
    def basic(self):
        """creates a very simple Jumbotron no header"""
        print('<div class="jumbotron">')
        print(self.text)
        print('</div><!--div for jumbotron-->')
    def withheader(self):
        """creates a jumbotron, method arguments:
        go in this order 
        1. THE TEXT 
        2. TITLE OF JUMBOTRON 
        3. HOW BIG YOU WANT THE HEADER """
        print('<div class="jumbotron">')
        print("<h", end='')
        print(self.h, end='') 
        print(">")
        print("\t",self.heading)
        print("</h", end='')
        print(self.h, end='') 
        print(">")
        print(self.text)
        print('</div><!--div for jumbotron-->')
               
class Image:
    """The only 1 argument is needed, everything else is broken into 
    first letter short hand. So arguments like this: 
    ('i.jpg',pull=l,resp=r,corner=t) will give you this:
    <a href="i.jpg" class="pull-left img-responsive corner-thumbnail/>
    """
    def __init__(self,img_src,*,img_alt='',pull='',resp='',corner=''):
        self.img_src=img_src
        self.img_alt=img_alt
        self.pull=pull
        self.resp=resp
        self.corner=corner        
        def img(self):
            img_build=[]
            img_build.append('<img src="'+self.img_src+'"')
            if self.img_alt !='':
                img_build.append('alt="'+self.img_alt+'"')
            if self.pull != '' or self.resp !='' or self.corner != '':
                e = 1
                img_build.append('class="')
                if self.pull == 'l':
                    img_build.append('pull-left')
                elif self.pull == 'r':
                    img_build.append('pull-right')
                if self.resp != '':
                    img_build.append('img-responsive')
                if self.corner =='c':
                    img_build.append('img-circle')
                elif self.corner =='r':
                    img_build.append('img-rounded')
                elif self.corner =='t':
                    img_build.append('img-rounded')
            for i in img_build:
                print(i, end=" ")
            if e !=1:
                print('/>')    
            elif e ==1:
                print('" />')

    
class BootstrapHtml:
    def __init__(self,title,tname,tplace,tag_title,tag_name,tag_place):
        self.title = title
        self.tname = tname
        self.tplace = tplace
        self.tag_title = tag_title
        self.tag_name = tag_name
        self.tag_place = tag_place 
    
    """ User needs to be asked what type of 
    tag before this can be used."""
    
    def build_lists(self):
        self.tag_title.append(self.title)
        self.tag_name.append(self.tname)        
        if self.tplace == '':
            self.tplace = "$@U!D0D00"
            self.tag_place.append(self.tplace)
        else:
            self.tag_place.append(self.tplace) 
        return self.tag_title, self.tag_name, self.tag_place
    
    """ Builds HTML tags """
    def tag_html(self):
        scount = len(self.tag_title)
        htm = []
        for n in range(0,scount,1):
            h = self.tag_title[n]+"<input type=\"text\" name=\""+self.tag_name[n]+"\" value=\"\" placeholder=\""+self.tag_place[n]+"\">"
            htm.append(h)
        return htm
    
    """ Builds HTML tags"""
    def das_boot(self):
        div_group = "\t"+'<div class="form-group thumbnail">'
        div_input = "\t\t"+'<div class="input-group">'
        div1 = "\t</div>"
        div2 = "\t\t</div>"
        scount = len(self.tag_title)
        bhtml=[]
        bhtml.append(div_group)
        for n in range(0,scount,1):
            bhtml.append(div_input)
            p1 = "\t\t\t<span class=\"input-group-addon\">"+self.tag_title[n]+"</span>"
            p2 = "\n\t\t\t<input type=\"text\" name=\""+self.tag_name[n]
            p3 = "\" value=\"\" placeholder=\""+self.tag_place[n]+"\">"
            bhtml.append(p1+p2+p3)
            bhtml.append(div2)
        bhtml.append(div1)
        return bhtml

class SubmitButton:
    def __init__(self,btype,bname,bvalue,btext):
        self.btype = btype
        self.bname = bname
        self.bvalue = bvalue
        self.btext = btext
    def submit_build(self):
        if self.btype.lower() == "h":
            button = "\t<button type=\"submit\" name=\""+self.bname+"\" value=\""+self.bvalue+"\">"+self.btext+"</button>"
        else:
            button = "\t<button type=\"submit\" class=\"btn btn-success\" name=\""+self.bname+"\" value=\""+self.bvalue+"\">"+self.btext+"</button>"
        return button

class FinalForm:
    def __init__(self,tag_type,action,method):
        self.tag_type = tag_type
        self.action = action
        self.method = method

    def form_build(self):
        if self.tag_type.lower() == "h":
            return "<form action=\""+self.action+"\" method=\""+self.method+"\">"

        else:
            return "<form action=\""+self.action+"\" method=\""+self.method+"\" role=\"form\">"
        
class CarouselEncoded:
    """
    ***This pic carousel requeire the module file_search.py
    
    Arguments needed:
        1st: The directory that the pictures are in. 
        2nd: File type.
    
    """
    def __init__(self,file_local, file_type):
        self.file_local=file_local
        self.file_type=file_type
    def pic_caro(self):
        so= file_search.FileSearch(self.file_local)
        jq_caro = """
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="bootstrap/js/jquery-1.7.2.min.js"><\/script>');</script>
        <script type="text/javascript">
            /* 
            timed 
            $('.carousel').carousel({
                  interval: 50000
                })
                */
            </script>
            <script> 
            /*
            paused
            */
              $(document).ready(function(){
                $('.carousel').carousel('pause');
              });
              
            $("#myCarousel").on('slide.bs.carousel', function(evt) {
              console.debug("slide transition started")
              console.debug('current slide = ', $(this).find('.active').index())
              console.debug('next slide = ', $(evt.relatedTarget).index())
            })
        </script>
        """
        caro_header = """
        <div class="row">
            <div class="col-sm-12 thumbnail">
        <!--  Carousel - consult the Twitter Bootstrap docs at
              http://twitter.github.com/bootstrap/javascript.html#carousel -->
            <div id="this-carousel-id" class="carousel slide"><!-- class of slide for animation -->
              <div class="carousel-inner">
        """
        
        caro_footer = """
            </div><!-- /.carousel-inner -->
              <!--  Next and Previous controls below
                    href values must reference the id for this carousel -->
              <!-- Controls -->
              <a class="left carousel-control" href="#this-carousel-id" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left"></span>
              </a>
              <a class="right carousel-control" href="#this-carousel-id" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right"></span>
              </a>
            </div><!-- /.carousel -->
            <p></p>
            </div>
        </div>
        """

        print(jq_caro)
        print(caro_header)
        
        for o in so.find_enc(self.file_type):
            if o == so.find_enc(self.file_type)[0]:
                print('<div class="item active">')
            else:
                print('<div class="item">')
            print("\t"+'<img src="/i_mage/pete_n_steve/book_1/'+o+'" alt="" class="img-responsive"/>')
            print("\t"+'<div class="carousel-caption">') 
            print("\t\t"+'<!--<p>Caption text here</p> -->')   
            print("\t"+'</div>')
            print('</div><!-- for item div-->')
        
        print(caro_footer)
