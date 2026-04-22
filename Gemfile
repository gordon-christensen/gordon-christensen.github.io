source "https://rubygems.org"

# Using the github-pages gem keeps versions aligned with what
# GitHub Pages actually builds in production.
gem "github-pages", group: :jekyll_plugins

# Windows & JRuby does not include zoneinfo files, so bundle them explicitly.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Windows-friendly file watcher
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
