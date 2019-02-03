--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4 (Debian 10.4-2.pgdg90+1)
-- Dumped by pg_dump version 10.5


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;

--
-- Config
--

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: geovote_back_4328
--

CREATE TABLE answer (
    id bigint NOT NULL,
    "finalCount" bigint,
    seals character varying(50)[],
    text text,
    "questionId" bigint NOT NULL
);

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: geovote_back_4328
--

CREATE SEQUENCE answer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geovote_back_4328
--

ALTER SEQUENCE answer_id_seq OWNED BY answer.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: geovote_back_4328
--

CREATE TABLE question (
    id bigint NOT NULL,
    "isPublic" boolean,
    "isPublished" boolean NOT NULL,
    latitude numeric(8,5),
    longitude numeric(8,5),
    "publishDuration" bigint NOT NULL,
    radius bigint,
    text text,
    "voteDate" timestamp without time zone NOT NULL,
    "voteDuration" bigint NOT NULL
);

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: geovote_back_4328
--

CREATE SEQUENCE question_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geovote_back_4328
--

ALTER SEQUENCE question_id_seq OWNED BY question.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: geovote_back_4328
--

ALTER TABLE ONLY answer ALTER COLUMN id SET DEFAULT nextval('answer_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: geovote_back_4328
--

ALTER TABLE ONLY question ALTER COLUMN id SET DEFAULT nextval('question_id_seq'::regclass);

--
-- Name: answer answer_pkey; Type: CONSTRAINT; Schema: public; Owner: geovote_back_4328
--

ALTER TABLE ONLY answer
    ADD CONSTRAINT answer_pkey PRIMARY KEY (id);


--
-- Name: question question_pkey; Type: CONSTRAINT; Schema: public; Owner: geovote_back_4328
--

ALTER TABLE ONLY question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);


--
-- Name: ix_answer_questionId; Type: INDEX; Schema: public; Owner: geovote_back_4328
--

CREATE INDEX "ix_answer_questionId" ON answer USING btree ("questionId");


--
-- Name: answer answer_questionId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: geovote_back_4328
--

ALTER TABLE ONLY answer
    ADD CONSTRAINT "answer_questionId_fkey" FOREIGN KEY ("questionId") REFERENCES question(id);


--
-- PostgreSQL database dump complete
--
