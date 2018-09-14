import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "enlaces_equipos"

    def start_requests(self):
        
        archivo = open("data/url_principal.csv", "r") #Lee la direccion principal y lo guarda en 'archivo'.
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        filename = ("data/urls_equipos.csv") #Crea un archivo csv llamado 'prefectos'
        datos = ("data/datos_equipos.csv")
        datos = codecs.open(datos, 'a', encoding='utf-8')
        datos.write('%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n'%('Equipo','Categoria','Presidente','Fundacion','Telefono','Fax','Sitio Web','Email','Campeonatos','Estadio','Capacidad','Direccion'))
          

        with codecs.open(filename, 'a', encoding='utf-8') as f:
            ul = response.xpath('//ul[@class="nav navbar-nav navbar-left visible-lg visible-md"]')
            li = ul.xpath('//li[@class="social-icons icons_separador"]')
            listaA = li[1].xpath('ul/li')
            for l in listaA:
                enlace = l.xpath('a/@href').extract()[0]
                f.write(u"http://www.ecuafutbol.org/web/%s\n" % (enlace)) 
            f.write(u"http://www.ecuafutbol.org/web/club.php?co=1890103746001\n")
            li = ul.xpath('//li[@class="social-icons"]')
            listaB = li[0].xpath('ul/li')
            for l in listaB:
                enlace = l.xpath('a/@href').extract()[0]
                f.write(u"http://www.ecuafutbol.org/web/%s\n" % (enlace))
            #filename.close()
        datos.close() 
        self.log('Saved file %s' % filename)
       
