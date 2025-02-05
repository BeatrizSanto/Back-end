package spring.boot.desafio.url.services;

import org.springframework.bens.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import spring.boot.desafio.url.repository.UrlRepository;


@Service
public class UrlService {

@Autowired
    private UrlRepository urlRepository;

    public String shortenUrl(String originalUrl) {

        String shortUrl = generateShortUrl();
        Url url = new Url ();
        url.setOriginalUrl(originalUrl);
        url.setShortUrl(shortUrl);
        url.setExpirationDate(LocalDateTime.now().plusDays(30));
        urlRepository.save(url);
        return shortUrl;
    }

    public  Optional<Url> getOriginalUrl(String.shortUrl){
        Optional<Url> urOptional = urlRepository.findByShortUrl(shortUrl);
        if (urOptional.isPresent()) {
            Url url = urOptional.get();
            if (url.getExpirationDate(),isAfter(LocalDateTime.now())){
                return Optional.of(url);
            }
            else{
                urlRepository.delete(url);
            }
            return Optional.empty();
        }
    }

    private String generateShortUrl() {
        String characteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        StringBuilder shortUrl = new StringBuilder();
        Random ranom = new Random();
        int length = 5 + ranom.nextInt(6);
        for  (int i = 0; i < length; i++){
            shortUrl.append(characteres.charAt(ranom.nextInt(characteres.length())));
        }
        return shortUrl.toString();
    }

}