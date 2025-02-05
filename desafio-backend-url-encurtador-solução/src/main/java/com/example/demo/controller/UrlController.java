package spring.boot.desafio.url.controller;

import spring.boot.desafio.url.services.UrlService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/url")
public class  UrlController{

    @Autowired
    private UrlService UrlService;

    @PostMapping ("/shorten")
    public ResponseEntity<map<String, String>>  shortenUrl(@RequestBody Map<String,String> request){
        String originalUrl = request.get("url");
        String shortUrl = UrlService.shortenUrl(originalUrl);
        Map<String,spring> response = new HashMap<String,String>();
        response.put("url", "https://xxx.com/" +shortenUrl);

        return ResponseEntity.ok(response);
    }

    @GetMapping("/shortUrl}")
    public ResponseEntity<object> redirectToOringalUrl(@PathVariable String shortUrl){

        Optional<Url> urOptional = UrlService.getOriginalUrl(shortUrl);
        if (urOptional.isPresent()){
            Url url = urOptional.get();
            System.out.println("Redirecionando para: "+url.getOriginalUrl());
            return  ResponseEntity.status(status:302).location(URI.create(url.getOriginalUrl())).build();
        }
        System.out.println("URL não encontrado ou expirado: "+shortUrl);
        return ResponseEntity.notFound().build();
    }

}