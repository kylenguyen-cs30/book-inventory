#!/bin/bash

# 1. Create 5 books
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

# 2. Get all books
echo -e "\nGetting all books..."
http GET http://localhost:8000/books/

# 3. Get individual books (1-5)
echo -e "\nGetting individual books..."
for i in {1..5}; do
	echo "Getting book $i:"
	http GET http://localhost:8000/books/$i
done

# 4. Update books with different scenarios
echo -e "\nUpdating books..."
echo "Updating book 1 (title only):"
http PUT http://localhost:8000/books/1 \
	title="The Great Gatsby (Revised)"

echo "Updating book 2 (multiple fields):"
http PUT http://localhost:8000/books/2 \
	title="To Kill a Mockingbird (2nd Edition)" \
	published_year:=1961

echo "Updating book 4 (with new ISBN):"
http PUT http://localhost:8000/books/4 \
	isbn="9780141439519" \
	title="Pride and Prejudice (Annotated)"

# 5. Verify updates
echo -e "\nVerifying updates..."
echo "Checking book 1:"
http GET http://localhost:8000/books/1
echo "Checking book 2:"
http GET http://localhost:8000/books/2
echo "Checking book 4:"
http GET http://localhost:8000/books/4

# 6. Delete a book
echo -e "\nDeleting book..."
echo "Deleting book 3:"
http DELETE http://localhost:8000/books/3

# 7. Final verification
echo -e "\nVerifying final book list..."
http GET http://localhost:8000/books/
