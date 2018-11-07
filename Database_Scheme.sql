--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.23
-- Dumped by pg_dump version 9.3.23
-- Started on 2018-11-07 16:08:08

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2002 (class 1262 OID 12029)
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Hungarian_Hungary.1250' LC_CTYPE = 'Hungarian_Hungary.1250';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2003 (class 0 OID 0)
-- Dependencies: 2002
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- TOC entry 2 (class 3079 OID 11750)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2006 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- TOC entry 1 (class 3079 OID 16384)
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- TOC entry 2007 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 174 (class 1259 OID 120401)
-- Name: articles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.articles (
    id integer NOT NULL,
    article text,
    used boolean
);


ALTER TABLE public.articles OWNER TO postgres;

--
-- TOC entry 173 (class 1259 OID 120399)
-- Name: articles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.articles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.articles_id_seq OWNER TO postgres;

--
-- TOC entry 2008 (class 0 OID 0)
-- Dependencies: 173
-- Name: articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.articles_id_seq OWNED BY public.articles.id;


--
-- TOC entry 176 (class 1259 OID 120421)
-- Name: corpus; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.corpus (
    id integer NOT NULL,
    data text,
    used boolean
);


ALTER TABLE public.corpus OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 120419)
-- Name: corpus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.corpus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.corpus_id_seq OWNER TO postgres;

--
-- TOC entry 2009 (class 0 OID 0)
-- Dependencies: 175
-- Name: corpus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.corpus_id_seq OWNED BY public.corpus.id;


--
-- TOC entry 178 (class 1259 OID 120531)
-- Name: loaded_sites; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.loaded_sites (
    site text
);


ALTER TABLE public.loaded_sites OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 120385)
-- Name: news_links; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.news_links (
    url character varying,
    used boolean,
    id integer NOT NULL
);


ALTER TABLE public.news_links OWNER TO postgres;

--
-- TOC entry 177 (class 1259 OID 120518)
-- Name: news_links_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.news_links_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.news_links_id_seq OWNER TO postgres;

--
-- TOC entry 2010 (class 0 OID 0)
-- Dependencies: 177
-- Name: news_links_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.news_links_id_seq OWNED BY public.news_links.id;


--
-- TOC entry 183 (class 1259 OID 123457)
-- Name: opinions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.opinions (
    id integer NOT NULL,
    positive numeric,
    negative numeric,
    transaction_code integer NOT NULL,
    filled boolean
);


ALTER TABLE public.opinions OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 123453)
-- Name: opinions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opinions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opinions_id_seq OWNER TO postgres;

--
-- TOC entry 2011 (class 0 OID 0)
-- Dependencies: 181
-- Name: opinions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opinions_id_seq OWNED BY public.opinions.id;


--
-- TOC entry 182 (class 1259 OID 123455)
-- Name: opinions_transaction_code_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.opinions_transaction_code_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.opinions_transaction_code_seq OWNER TO postgres;

--
-- TOC entry 2012 (class 0 OID 0)
-- Dependencies: 182
-- Name: opinions_transaction_code_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.opinions_transaction_code_seq OWNED BY public.opinions.transaction_code;


--
-- TOC entry 187 (class 1259 OID 123972)
-- Name: result_cache; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.result_cache (
    id integer NOT NULL,
    expression text,
    positive_percent integer
);


ALTER TABLE public.result_cache OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 123970)
-- Name: result_cache_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.result_cache_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.result_cache_id_seq OWNER TO postgres;

--
-- TOC entry 2013 (class 0 OID 0)
-- Dependencies: 186
-- Name: result_cache_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.result_cache_id_seq OWNED BY public.result_cache.id;


--
-- TOC entry 185 (class 1259 OID 123900)
-- Name: searched_expression; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.searched_expression (
    id integer NOT NULL,
    expression text
);


ALTER TABLE public.searched_expression OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 123898)
-- Name: searched_expression_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.searched_expression_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.searched_expression_id_seq OWNER TO postgres;

--
-- TOC entry 2014 (class 0 OID 0)
-- Dependencies: 184
-- Name: searched_expression_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.searched_expression_id_seq OWNED BY public.searched_expression.id;


--
-- TOC entry 180 (class 1259 OID 123267)
-- Name: selected_articles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.selected_articles (
    id integer NOT NULL,
    article text
);


ALTER TABLE public.selected_articles OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 123265)
-- Name: selected_articles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.selected_articles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.selected_articles_id_seq OWNER TO postgres;

--
-- TOC entry 2015 (class 0 OID 0)
-- Dependencies: 179
-- Name: selected_articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.selected_articles_id_seq OWNED BY public.selected_articles.id;


--
-- TOC entry 1875 (class 2604 OID 120404)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.articles ALTER COLUMN id SET DEFAULT nextval('public.articles_id_seq'::regclass);


--
-- TOC entry 1876 (class 2604 OID 120424)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.corpus ALTER COLUMN id SET DEFAULT nextval('public.corpus_id_seq'::regclass);


--
-- TOC entry 1874 (class 2604 OID 120520)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.news_links ALTER COLUMN id SET DEFAULT nextval('public.news_links_id_seq'::regclass);


--
-- TOC entry 1878 (class 2604 OID 123460)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opinions ALTER COLUMN id SET DEFAULT nextval('public.opinions_id_seq'::regclass);


--
-- TOC entry 1879 (class 2604 OID 123461)
-- Name: transaction_code; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.opinions ALTER COLUMN transaction_code SET DEFAULT nextval('public.opinions_transaction_code_seq'::regclass);


--
-- TOC entry 1881 (class 2604 OID 123975)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.result_cache ALTER COLUMN id SET DEFAULT nextval('public.result_cache_id_seq'::regclass);


--
-- TOC entry 1880 (class 2604 OID 123903)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.searched_expression ALTER COLUMN id SET DEFAULT nextval('public.searched_expression_id_seq'::regclass);


--
-- TOC entry 1877 (class 2604 OID 123270)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.selected_articles ALTER COLUMN id SET DEFAULT nextval('public.selected_articles_id_seq'::regclass);


--
-- TOC entry 1883 (class 2606 OID 120409)
-- Name: articles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_pkey PRIMARY KEY (id);


--
-- TOC entry 1885 (class 2606 OID 120429)
-- Name: corpus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.corpus
    ADD CONSTRAINT corpus_pkey PRIMARY KEY (id);


--
-- TOC entry 1889 (class 2606 OID 123466)
-- Name: opinions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.opinions
    ADD CONSTRAINT opinions_pkey PRIMARY KEY (id);


--
-- TOC entry 1887 (class 2606 OID 123275)
-- Name: selected_articles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.selected_articles
    ADD CONSTRAINT selected_articles_pkey PRIMARY KEY (id);


--
-- TOC entry 2005 (class 0 OID 0)
-- Dependencies: 7
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2018-11-07 16:08:08

--
-- PostgreSQL database dump complete
--

