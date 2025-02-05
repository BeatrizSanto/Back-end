package spring.boot.desafio.url.model;

import jakarta.time.LocalDateTime;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence,GenerationType;
import jakarta.persistence.id;
import lombok.Getter;
import lombok.Setter;



@Entity
@Getter
@Setter
public class Url{

    @id
    @GeneratedValue(strategy = GenerationType.IDENTITY)

    private Long id;

    private String originalUrl;

    private String shortUrl;

    private LocalDateTime expirationDate;

}