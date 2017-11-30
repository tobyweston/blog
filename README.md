## bad.robot

The source for [http://baddotrobot.com](http://baddotrobot.com), forked from [Octopress](http://octopress.org/).

Octopress is [Jekyll](https://github.com/mojombo/jekyll) blogging at its finest.

### Reminder for Forgetful Me

    rake clean
    rake new_post["title"]
    rake preview
    rake generate
    rake deploy

The preview site is [http://localhost:4000/](http://localhost:4000/).

### Deploying

There's a bunch of stuff to consider when deploying to Github Pages.

See the [Ocotopress site](http://octopress.org/docs/deploying/github/).

The main thing to note is that the `_deploy` folder isn't committed to `master`. Instead, it should be an independent clone of the `gh-pages` branch. The `rake deploy` will copy generated artifacts (the `public` folder) into it and commit and push it (where Github Pages pick it up and deploy proper).

Run the following to bootstrap it.

```
rm -rf _deploy
git clone git@github.com:tobyweston/blog.git _deploy
cd _deploy
git checkout gh-pages
```

### Setup

If you're using Homebrew:

* See what's installed with `brew list`
* install Ruby with `brew install ruby`
* If you get errors like `LoadError: cannot load such file -- bundler/setup`, run `gem install bundler & bundle install`
* The `Gemfile.lock` has the versions of dependencies from the last time you ran the bundle install command(?), delete it and let `bundle install` regenerate it (with more recent versions) if you need to.

#### My Crapy Ruby Install Log 

Might be useful in some future where things don't work.

```
$ brew install ruby
...
==> Installing dependencies for ruby: readline, libyaml, openssl
==> Installing ruby dependency: readline
==> Downloading https://homebrew.bintray.com/bottles/readline-7.0.3_1.high_sierra.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/45/45322d69fba127fe9d5c8d1d2fe8b57e0a657b0ebc0a8143cc47118243828dfd?__gda__=exp=151205
######################################################################## 100.0%
==> Pouring readline-7.0.3_1.high_sierra.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local,
because macOS provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only..

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/readline/lib
    CPPFLAGS: -I/usr/local/opt/readline/include

==> Summary
🍺  /usr/local/Cellar/readline/7.0.3_1: 46 files, 1.5MB
==> Installing ruby dependency: libyaml
==> Downloading https://homebrew.bintray.com/bottles/libyaml-0.1.7.high_sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libyaml-0.1.7.high_sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libyaml/0.1.7: 9 files, 299.8KB
==> Installing ruby dependency: openssl
==> Downloading https://homebrew.bintray.com/bottles/openssl-1.0.2m.high_sierra.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/0e/0eeee936b7f362ec5d2d844deb74ec92b79d3105445e5ca5e8767df4aabdebfd?__gda__=exp=151205
######################################################################## 100.0%
==> Pouring openssl-1.0.2m.high_sierra.bottle.tar.gz
==> Caveats
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

This formula is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have this software first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include

==> Summary
🍺  /usr/local/Cellar/openssl/1.0.2m: 1,792 files, 12.3MB
==> Installing ruby
==> Downloading https://homebrew.bintray.com/bottles/ruby-2.4.2_1.high_sierra.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/5a/5a1d5adf5f9b0f151a484edcc292764a0b0dbef61eb667c59aa850d0ad3d7626?__gda__=exp=151205
######################################################################## 100.0%
==> Pouring ruby-2.4.2_1.high_sierra.bottle.tar.gz
==> Caveats
Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/ruby
==> Summary
🍺  /usr/local/Cellar/ruby/2.4.2_1: 3,042 files, 16.3MB
```

I had an old (default Mac installed?) version:

```
$ ruby --version
ruby 2.3.3p222 (2016-11-21 revision 56859) [universal.x86_64-darwin17]
```

Which got upgraded to:
```
$ ruby --version
ruby 2.4.2p198 (2017-09-14 revision 59899) [x86_64-darwin17]
```