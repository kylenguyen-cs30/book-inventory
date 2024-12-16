#!/bin/bash

echo "Creating books..."
echo "Creating book 1: The Great Gatsby"
http POST http://localhost:8000/books/ \
	title="The Great Gatsby" \
	author="F. Scott Fitzgerald" \
	isbn="9780743273565" \
	published_year:=1925

echo "Creating book 2: To Kill a Mockingbird"
http POST http://localhost:8000/books/ \
	title="To Kill a Mockingbird" \
	author="Harper Lee" \
	isbn="9780446310789" \
	published_year:=1960

echo "Creating book 3: 1984"
http POST http://localhost:8000/books/ \
	title="1984" \
	author="George Orwell" \
	isbn="9780451524935" \
	published_year:=1949

echo "Creating book 4: Pride and Prejudice"
http POST http://localhost:8000/books/ \
	title="Pride and Prejudice" \
	author="Jane Austen" \
	isbn="9780141439518" \
	published_year:=1813

echo "Creating book 5: The Catcher in the Rye"
http POST http://localhost:8000/books/ \
	title="The Catcher in the Rye" \
	author="J.D. Salinger" \
	isbn="9780316769488" \
	published_year:=1951
