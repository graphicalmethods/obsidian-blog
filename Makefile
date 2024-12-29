# Define the directories to be created
DIRS = assets/css assets/images _data _drafts _includes _layouts _posts

# Create directories
dirs:
	@echo "Creating directories..."
	@mkdir -p $(DIRS)
	@echo "Directories created successfully."

# Clean up (remove all directories)
clean:
	@echo "Cleaning up..."
	@rm -rf assets _data _drafts _includes _layouts _posts
	@echo "Cleanup complete."

start_server:
	@bundle exec jekyll s

convert_images:
	@source venv/bin/activate
	@python image-conversion.py

date = $(shell date +"%Y-%m-%d")
TITLE = test-title  # You can set this to whatever title you want
filename = ./_posts/$(date)-$(TITLE).md
create_post:
ifndef TITLE
	$(error TITLE is not defined. Usage: make create_post TITLE="Your Title Here")
endif
	@echo "---" > $(filename)
	@echo "title:" >> $(filename)
	@echo "description:" >> $(filename)
	@echo "layout: posts" >> $(filename)
	@echo "---" >> $(filename)
	@echo "Created file: $(filename)"
