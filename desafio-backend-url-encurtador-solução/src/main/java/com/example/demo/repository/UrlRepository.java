package spring.boot.desafio.url.repository;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

import spring.boot.desafio.url.model.Url;

public interface UrlRepository extends JpaRepository<Url,Long> {

    Optional<Url> findByShortUrl(String shortUrl);

}
