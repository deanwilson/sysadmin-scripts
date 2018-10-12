#!/usr/bin/perl
use strict;
use warnings;
use Net::Domain::ExpireDate;

die "$0: <file of domainnames>\n" unless @ARGV == 1;

my $domainfile = shift;

open( my $domains_fh, '<', $domainfile )
  || die "Failed to open [$domainfile]: $!\n";

my %domain_expiry;
for my $domain ( sort <$domains_fh> ) {
  my $expiration = expire_date( $domain, '%Y-%m-%d' );

  $expiration ||= "unknown";

  push @{ $domain_expiry{$expiration} }, $domain;
}

for my $expiry_date (sort keys %domain_expiry) {
  print "$expiry_date -\n";
  print "  --  $_" for  @{ $domain_expiry{$expiry_date} };
}
