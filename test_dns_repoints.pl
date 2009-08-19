#!/usr/bin/perl -w
use strict;
use warnings;
use File::Slurp;
use Net::DNS;
use Test::More qw(no_plan);
use URI::Title qw( title );

# this script is quite simple and (on purpose) doesn't deal with names that
# return more than one ip address. Change the call to get_ip to return an
# array of ips and loop over that if you need it.

die "$0: <desired_ip> <title_substring> <file of domains>\n" unless @ARGV == 3;

my $desired_ip    = shift; # IP the sites should point to
my $desired_title = shift; # substring in title all the sites should have
my $domainfile    = shift; # file of one domain per line

my $res = Net::DNS::Resolver->new;

my @domains = read_file( $domainfile ) ;

for my $domain ( sort @domains ) {
  chomp $domain;

  is( get_ip($domain), $desired_ip, "Resolve [$domain] to [$desired_ip]" );

  my $title = title("http://$domain");
  like($title, qr/$desired_title/, "Title should contain [$desired_title]" );
}

######################################################################

sub get_ip {
  my $hostname = shift;
  my $query    = $res->search( $hostname );

  if ($query) {
    foreach my $rr ( $query->answer ) {
      next unless $rr->type eq "A";
      # return the first answer
      return $rr->address;
    }
  } else {
    return "Query failed: ", $res->errorstring;
  }
}
