--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Actor; Type: TABLE; Schema: public; Owner: reemaalhassan
--

CREATE TABLE public."Actor" (
    id integer NOT NULL,
    name character varying(120),
    age integer,
    gender character varying(120)
);


ALTER TABLE public."Actor" OWNER TO reemaalhassan;

--
-- Name: Actor_id_seq; Type: SEQUENCE; Schema: public; Owner: reemaalhassan
--

CREATE SEQUENCE public."Actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actor_id_seq" OWNER TO reemaalhassan;

--
-- Name: Actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: reemaalhassan
--

ALTER SEQUENCE public."Actor_id_seq" OWNED BY public."Actor".id;


--
-- Name: Movie; Type: TABLE; Schema: public; Owner: reemaalhassan
--

CREATE TABLE public."Movie" (
    id integer NOT NULL,
    title character varying(120),
    release_date date
);


ALTER TABLE public."Movie" OWNER TO reemaalhassan;

--
-- Name: Movie_id_seq; Type: SEQUENCE; Schema: public; Owner: reemaalhassan
--

CREATE SEQUENCE public."Movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movie_id_seq" OWNER TO reemaalhassan;

--
-- Name: Movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: reemaalhassan
--

ALTER SEQUENCE public."Movie_id_seq" OWNED BY public."Movie".id;


--
-- Name: Actor id; Type: DEFAULT; Schema: public; Owner: reemaalhassan
--

ALTER TABLE ONLY public."Actor" ALTER COLUMN id SET DEFAULT nextval('public."Actor_id_seq"'::regclass);


--
-- Name: Movie id; Type: DEFAULT; Schema: public; Owner: reemaalhassan
--

ALTER TABLE ONLY public."Movie" ALTER COLUMN id SET DEFAULT nextval('public."Movie_id_seq"'::regclass);


--
-- Data for Name: Actor; Type: TABLE DATA; Schema: public; Owner: reemaalhassan
--

COPY public."Actor" (id, name, age, gender) FROM stdin;
1	Jennifer aniston	51	Female
2	Will smith	52	Male
3	Leonardo dicaprio	46	Male
4	Brad pitt	57	Male
5	Tom hanks	64	Male
\.


--
-- Data for Name: Movie; Type: TABLE DATA; Schema: public; Owner: reemaalhassan
--

COPY public."Movie" (id, title, release_date) FROM stdin;
1	Mulan	2020-01-01
2	The Midnight Sky	2020-01-01
3	Inception	2010-01-01
4	Tenet	2020-01-01
5	Joker	2019-01-01
\.


--
-- Name: Actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: reemaalhassan
--

SELECT pg_catalog.setval('public."Actor_id_seq"', 5, true);


--
-- Name: Movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: reemaalhassan
--

SELECT pg_catalog.setval('public."Movie_id_seq"', 5, true);


--
-- Name: Actor Actor_pkey; Type: CONSTRAINT; Schema: public; Owner: reemaalhassan
--

ALTER TABLE ONLY public."Actor"
    ADD CONSTRAINT "Actor_pkey" PRIMARY KEY (id);


--
-- Name: Movie Movie_pkey; Type: CONSTRAINT; Schema: public; Owner: reemaalhassan
--

ALTER TABLE ONLY public."Movie"
    ADD CONSTRAINT "Movie_pkey" PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

