# Init SQLAlchemy ORM

# Importa le dipendenze

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, BIGINT, VARCHAR, TEXT, JSON

# Definisco le astrazioni delle tabelle (ORM)

class Base(DeclarativeBase):
    pass

class Nazione(Base):
    __tablename__ = "nazione"
    id: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True), primary_key=True)
    codice_2_caratteri: Mapped[str] = mapped_column(VARCHAR(255))
    codice_3_caratteri: Mapped[str] = mapped_column(VARCHAR(255))
    codice_numerico: Mapped[int] = mapped_column(INTEGER(11))

    url: Mapped["URL"] = relationship(back_populates="url")

class Pagamento(Base):
    __tablename__ = "pagamento"
    id: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True), primary_key=True)
    nome: Mapped[str] = mapped_column(VARCHAR(255), unique=True)
    descrizione: Mapped[str] = mapped_column(TEXT)
    attivo: Mapped[bool] = mapped_column(TINYINT(1), default=0)

    url: Mapped["URL"] = relationship(back_populates="url")

class Motore(Base):
    __tablename__ = "motore"
    id: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True), primary_key=True)
    nome: Mapped[str] = mapped_column(VARCHAR(255), unique=True)
    descrizione: Mapped[str] = mapped_column(TEXT)

    url: Mapped["URL"] = relationship(back_populates="url")

class Rotta(Base):
    __tablename__ = "rotta"
    id: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True), primary_key=True)
    successo: Mapped[str] = mapped_column(TEXT)
    annullamento: Mapped[str] = mapped_column(TEXT)
    webhook: Mapped[str] = mapped_column(TEXT)
    pagina_pagamento: Mapped[str] = mapped_column(TEXT)

    url: Mapped["URL"] = relationship(back_populates="url")

class Versione(Base):
    __tablename__ = "versione"
    id: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True), primary_key=True)
    crea_pagamento: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True))
    recupera_pagamento: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True))
    esegui_pagamento: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True))
    verifica_pagamento: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True))

    url: Mapped["URL"] = relationship(back_populates="url")

class URL(Base):
    __tablename__ = "url"
    id: Mapped[int] = mapped_column(BIGINT(display_width=22, unsigned=True), primary_key=True)
    id_rotta: Mapped[int] = mapped_column(ForeignKey("rotta.id"))
    id_versione: Mapped[int] = mapped_column(ForeignKey("versione.id"))
    id_nazione: Mapped[int] = mapped_column(ForeignKey("nazione.id"))
    id_pagamento: Mapped[int] = mapped_column(ForeignKey("pagamento.id"))
    id_motore: Mapped[int] = mapped_column(ForeignKey("motore.id"))
    meta: Mapped[str] = mapped_column(JSON, nullable=True)
    test: Mapped[bool] = mapped_column(TINYINT(1), default=0)

    rotta: Mapped["Rotta"] = relationship(back_populates="rotta")
    versione: Mapped["Versione"] = relationship(back_populates="versione")
    nazione: Mapped["Nazione"] = relationship(back_populates="nazione")
    pagamento: Mapped["Pagamento"] = relationship(back_populates="pagamento")
    motore: Mapped["Motore"] = relationship(back_populates="motore")