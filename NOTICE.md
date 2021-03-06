# NOTICES

This repository incorporates material as listed below or described in the code

## Python 3

### License

    1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
    the Individual or Organization ("Licensee") accessing and otherwise using Python
    3.9.6 software in source or binary form and its associated documentation.

    2. Subject to the terms and conditions of this License Agreement, PSF hereby
    grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
    analyze, test, perform and/or display publicly, prepare derivative works,
    distribute, and otherwise use Python 3.9.6 alone or in any derivative
    version, provided, however, that PSF's License Agreement and PSF's notice of
    copyright, i.e., "Copyright © 2001-2021 Python Software Foundation; All Rights
    Reserved" are retained in Python 3.9.6 alone or in any derivative version
    prepared by Licensee.

    3. In the event Licensee prepares a derivative work that is based on or
    incorporates Python 3.9.6 or any part thereof, and wants to make the
    derivative work available to others as provided herein, then Licensee hereby
    agrees to include in any such work a brief summary of the changes made to Python
    3.9.6.

    4. PSF is making Python 3.9.6 available to Licensee on an "AS IS" basis.
    PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
    EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
    WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
    USE OF PYTHON 3.9.6 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

    5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.9.6
    FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
    MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.9.6, OR ANY DERIVATIVE
    THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

    6. This License Agreement will automatically terminate upon a material breach of
    its terms and conditions.

    7. Nothing in this License Agreement shall be deemed to create any relationship
    of agency, partnership, or joint venture between PSF and Licensee.  This License
    Agreement does not grant permission to use PSF trademarks or trade name in a
    trademark sense to endorse or promote products or services of Licensee, or any
    third party.

    8. By copying, installing or otherwise using Python 3.9.6, Licensee agrees
    to be bound by the terms and conditions of this License Agreement.

### Aditional Attributions
#### Mersenne Twister
The _random module includes code based on a download from http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/emt19937ar.html. The following are the verbatim comments from the original code:

A C-program for MT19937, with initialization improved 2002/1/26.
Coded by Takuji Nishimura and Makoto Matsumoto.

Before using, initialize the state by using init_genrand(seed)
or init_by_array(init_key, key_length).

    Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

    1. Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.

    3. The names of its contributors may not be used to endorse or promote
        products derived from this software without specific prior written
        permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
    CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
    NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


    Any feedback is very welcome.
    http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html
    email: m-mat @ math.sci.hiroshima-u.ac.jp (remove space)

#### Sockets
The socket module uses the functions, getaddrinfo(), and getnameinfo(), which are coded in separate source files from the WIDE Project, http://www.wide.ad.jp/.

    Copyright (C) 1995, 1996, 1997, and 1998 WIDE Project.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:
    1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
    3. Neither the name of the project nor the names of its contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.


#### Asynchronous socket services
The asynchat and asyncore modules contain the following notice:

    Copyright 1996 by Sam Rushing

                            All Rights Reserved

    Permission to use, copy, modify, and distribute this software and
    its documentation for any purpose and without fee is hereby
    granted, provided that the above copyright notice appear in all
    copies and that both that copyright notice and this permission
    notice appear in supporting documentation, and that the name of Sam
    Rushing not be used in advertising or publicity pertaining to
    distribution of the software without specific, written prior
    permission.

    SAM RUSHING DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
    INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
    NO EVENT SHALL SAM RUSHING BE LIABLE FOR ANY SPECIAL, INDIRECT OR
    CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
    OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
    NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
    CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

#### Cookie management
The http.cookies module contains the following notice:

    Copyright 2000 by Timothy O'Malley <timo@alum.mit.edu>

                All Rights Reserved

    Permission to use, copy, modify, and distribute this software
    and its documentation for any purpose and without fee is hereby
    granted, provided that the above copyright notice appear in all
    copies and that both that copyright notice and this permission
    notice appear in supporting documentation, and that the name of
    Timothy O'Malley  not be used in advertising or publicity
    pertaining to distribution of the software without specific, written
    prior permission.

    Timothy O'Malley DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
    SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS, IN NO EVENT SHALL Timothy O'Malley BE LIABLE FOR
    ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
    WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
    ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
    PERFORMANCE OF THIS SOFTWARE.

#### Execution tracing
The trace module contains the following notice:

    portions copyright 2001, Autonomous Zones Industries, Inc., all rights...
    err...  reserved and offered to the public under the terms of the
    Python 2.2 license.
    Author: Zooko O'Whielacronx
    http://zooko.com/
    mailto:zooko@zooko.com

    Copyright 2000, Mojam Media, Inc., all rights reserved.
    Author: Skip Montanaro

    Copyright 1999, Bioreason, Inc., all rights reserved.
    Author: Andrew Dalke

    Copyright 1995-1997, Automatrix, Inc., all rights reserved.
    Author: Skip Montanaro

    Copyright 1991-1995, Stichting Mathematisch Centrum, all rights reserved.


    Permission to use, copy, modify, and distribute this Python software and
    its associated documentation for any purpose without fee is hereby
    granted, provided that the above copyright notice appears in all copies,
    and that both that copyright notice and this permission notice appear in
    supporting documentation, and that the name of neither Automatrix,
    Bioreason or Mojam Media be used in advertising or publicity pertaining to
    distribution of the software without specific, written prior permission.

#### UUencode and UUdecode functions
The uu module contains the following notice:

    Copyright 1994 by Lance Ellinghouse
    Cathedral City, California Republic, United States of America.
                        All Rights Reserved
    Permission to use, copy, modify, and distribute this software and its
    documentation for any purpose and without fee is hereby granted,
    provided that the above copyright notice appear in all copies and that
    both that copyright notice and this permission notice appear in
    supporting documentation, and that the name of Lance Ellinghouse
    not be used in advertising or publicity pertaining to distribution
    of the software without specific, written prior permission.
    LANCE ELLINGHOUSE DISCLAIMS ALL WARRANTIES WITH REGARD TO
    THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
    FITNESS, IN NO EVENT SHALL LANCE ELLINGHOUSE CENTRUM BE LIABLE
    FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
    OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

    Modified by Jack Jansen, CWI, July 1995:
    - Use binascii module to do the actual line-by-line conversion
    between ascii and binary. This results in a 1000-fold speedup. The C
    version is still 5 times faster, though.
    - Arguments more compliant with Python standard

#### XML Remote Procedure Calls
The xmlrpc.client module contains the following notice:

        The XML-RPC client interface is

    Copyright (c) 1999-2002 by Secret Labs AB
    Copyright (c) 1999-2002 by Fredrik Lundh

    By obtaining, using, and/or copying this software and/or its
    associated documentation, you agree that you have read, understood,
    and will comply with the following terms and conditions:

    Permission to use, copy, modify, and distribute this software and
    its associated documentation for any purpose and without fee is
    hereby granted, provided that the above copyright notice appears in
    all copies, and that both that copyright notice and this permission
    notice appear in supporting documentation, and that the name of
    Secret Labs AB or the author not be used in advertising or publicity
    pertaining to distribution of the software without specific, written
    prior permission.

    SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD
    TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-
    ABILITY AND FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR
    BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY
    DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,
    WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
    ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
    OF THIS SOFTWARE.

#### test_epoll
The test_epoll module contains the following notice:

    Copyright (c) 2001-2006 Twisted Matrix Laboratories.

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
    OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#### Select kqueue
The select module contains the following notice for the kqueue interface:

    Copyright (c) 2000 Doug White, 2006 James Knight, 2007 Christian Heimes
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:
    1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.

#### SipHash24
The file Python/pyhash.c contains Marek Majkowski’ implementation of Dan Bernstein’s SipHash24 algorithm. It contains the following note:

    <MIT License>
    Copyright (c) 2013  Marek Majkowski <marek@popcount.org>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    </MIT License>

    Original location:
    https://github.com/majek/csiphash/

    Solution inspired by code from:
    Samuel Neves (supercop/crypto_auth/siphash24/little)
    djb (supercop/crypto_auth/siphash24/little2)
    Jean-Philippe Aumasson (https://131002.net/siphash/siphash24.c)

#### strtod and dtoa
The file Python/dtoa.c, which supplies C functions dtoa and strtod for conversion of C doubles to and from strings, is derived from the file of the same name by David M. Gay, currently available from http://www.netlib.org/fp/. The original file, as retrieved on March 16, 2009, contains the following copyright and licensing notice:

    /****************************************************************
    *
    * The author of this software is David M. Gay.
    *
    * Copyright (c) 1991, 2000, 2001 by Lucent Technologies.
    *
    * Permission to use, copy, modify, and distribute this software for any
    * purpose without fee is hereby granted, provided that this entire notice
    * is included in all copies of any software which is or includes a copy
    * or modification of this software and in all copies of the supporting
    * documentation for such software.
    *
    * THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
    * WARRANTY.  IN PARTICULAR, NEITHER THE AUTHOR NOR LUCENT MAKES ANY
    * REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
    * OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.
    *
    ***************************************************************/

#### OpenSSL
The modules hashlib, posix, ssl, crypt use the OpenSSL library for added performance if made available by the operating system. Additionally, the Windows and Mac OS X installers for Python may include a copy of the OpenSSL libraries, so we include a copy of the OpenSSL license here:

    LICENSE ISSUES
    ==============

    The OpenSSL toolkit stays under a dual license, i.e. both the conditions of
    the OpenSSL License and the original SSLeay license apply to the toolkit.
    See below for the actual license texts. Actually both licenses are BSD-style
    Open Source licenses. In case of any license issues related to OpenSSL
    please contact openssl-core@openssl.org.

    OpenSSL License
    ---------------

    /* ====================================================================
        * Copyright (c) 1998-2008 The OpenSSL Project.  All rights reserved.
        *
        * Redistribution and use in source and binary forms, with or without
        * modification, are permitted provided that the following conditions
        * are met:
        *
        * 1. Redistributions of source code must retain the above copyright
        *    notice, this list of conditions and the following disclaimer.
        *
        * 2. Redistributions in binary form must reproduce the above copyright
        *    notice, this list of conditions and the following disclaimer in
        *    the documentation and/or other materials provided with the
        *    distribution.
        *
        * 3. All advertising materials mentioning features or use of this
        *    software must display the following acknowledgment:
        *    "This product includes software developed by the OpenSSL Project
        *    for use in the OpenSSL Toolkit. (http://www.openssl.org/)"
        *
        * 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
        *    endorse or promote products derived from this software without
        *    prior written permission. For written permission, please contact
        *    openssl-core@openssl.org.
        *
        * 5. Products derived from this software may not be called "OpenSSL"
        *    nor may "OpenSSL" appear in their names without prior written
        *    permission of the OpenSSL Project.
        *
        * 6. Redistributions of any form whatsoever must retain the following
        *    acknowledgment:
        *    "This product includes software developed by the OpenSSL Project
        *    for use in the OpenSSL Toolkit (http://www.openssl.org/)"
        *
        * THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
        * EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
        * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
        * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE OpenSSL PROJECT OR
        * ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
        * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
        * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
        * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
        * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
        * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
        * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
        * OF THE POSSIBILITY OF SUCH DAMAGE.
        * ====================================================================
        *
        * This product includes cryptographic software written by Eric Young
        * (eay@cryptsoft.com).  This product includes software written by Tim
        * Hudson (tjh@cryptsoft.com).
        *
        */

    Original SSLeay License
    -----------------------

    /* Copyright (C) 1995-1998 Eric Young (eay@cryptsoft.com)
        * All rights reserved.
        *
        * This package is an SSL implementation written
        * by Eric Young (eay@cryptsoft.com).
        * The implementation was written so as to conform with Netscapes SSL.
        *
        * This library is free for commercial and non-commercial use as long as
        * the following conditions are aheared to.  The following conditions
        * apply to all code found in this distribution, be it the RC4, RSA,
        * lhash, DES, etc., code; not just the SSL code.  The SSL documentation
        * included with this distribution is covered by the same copyright terms
        * except that the holder is Tim Hudson (tjh@cryptsoft.com).
        *
        * Copyright remains Eric Young's, and as such any Copyright notices in
        * the code are not to be removed.
        * If this package is used in a product, Eric Young should be given attribution
        * as the author of the parts of the library used.
        * This can be in the form of a textual message at program startup or
        * in documentation (online or textual) provided with the package.
        *
        * Redistribution and use in source and binary forms, with or without
        * modification, are permitted provided that the following conditions
        * are met:
        * 1. Redistributions of source code must retain the copyright
        *    notice, this list of conditions and the following disclaimer.
        * 2. Redistributions in binary form must reproduce the above copyright
        *    notice, this list of conditions and the following disclaimer in the
        *    documentation and/or other materials provided with the distribution.
        * 3. All advertising materials mentioning features or use of this software
        *    must display the following acknowledgement:
        *    "This product includes cryptographic software written by
        *     Eric Young (eay@cryptsoft.com)"
        *    The word 'cryptographic' can be left out if the rouines from the library
        *    being used are not cryptographic related :-).
        * 4. If you include any Windows specific code (or a derivative thereof) from
        *    the apps directory (application code) you must include an acknowledgement:
        *    "This product includes software written by Tim Hudson (tjh@cryptsoft.com)"
        *
        * THIS SOFTWARE IS PROVIDED BY ERIC YOUNG ``AS IS'' AND
        * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
        * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
        * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
        * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
        * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
        * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
        * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
        * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
        * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
        * SUCH DAMAGE.
        *
        * The licence and distribution terms for any publically available version or
        * derivative of this code cannot be changed.  i.e. this code cannot simply be
        * copied and put under another distribution licence
        * [including the GNU Public Licence.]
        */

#### expat
The pyexpat extension is built using an included copy of the expat sources unless the build is configured --with-system-expat:

    Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
                                and Clark Cooper

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#### libffi
The _ctypes extension is built using an included copy of the libffi sources unless the build is configured --with-system-libffi:

    Copyright (c) 1996-2008  Red Hat, Inc and others.

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    ``Software''), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED ``AS IS'', WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

#### zlib
The zlib extension is built using an included copy of the zlib sources if the zlib version found on the system is too old to be used for the build:

    Copyright (C) 1995-2011 Jean-loup Gailly and Mark Adler

    This software is provided 'as-is', without any express or implied
    warranty.  In no event will the authors be held liable for any damages
    arising from the use of this software.

    Permission is granted to anyone to use this software for any purpose,
    including commercial applications, and to alter it and redistribute it
    freely, subject to the following restrictions:

    1. The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software
    in a product, an acknowledgment in the product documentation would be
    appreciated but is not required.

    2. Altered source versions must be plainly marked as such, and must not be
    misrepresented as being the original software.

    3. This notice may not be removed or altered from any source distribution.

    Jean-loup Gailly        Mark Adler
    jloup@gzip.org          madler@alumni.caltech.edu

#### cfuhash
The implementation of the hash table used by the tracemalloc is based on the cfuhash project:

    Copyright (c) 2005 Don Owens
    All rights reserved.

    This code is released under the BSD license:

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

    * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
        copyright notice, this list of conditions and the following
        disclaimer in the documentation and/or other materials provided
        with the distribution.

    * Neither the name of the author nor the names of its
        contributors may be used to endorse or promote products derived
        from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
    STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
    OF THE POSSIBILITY OF SUCH DAMAGE.

#### libmpdec
The _decimal module is built using an included copy of the libmpdec library unless the build is configured --with-system-libmpdec:

    Copyright (c) 2008-2020 Stefan Krah. All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

    1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
    HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
    OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
    SUCH DAMAGE.

#### W3C C14N test suite
The C14N 2.0 test suite in the test package (Lib/test/xmltestdata/c14n-20/) was retrieved from the W3C website at https://www.w3.org/TR/xml-c14n2-testcases/ and is distributed under the 3-clause BSD license:

    Copyright (c) 2013 W3C(R) (MIT, ERCIM, Keio, Beihang),
    All Rights Reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

    * Redistributions of works must retain the original copyright notice,
    this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the original copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
    * Neither the name of the W3C nor the names of its contributors may be
    used to endorse or promote products derived from this work without
    specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## pyserial

### License

    Copyright (c) 2001-2020 Chris Liechti <cliechti@gmx.net>
    All Rights Reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
        copyright notice, this list of conditions and the following
        disclaimer in the documentation and/or other materials provided
        with the distribution.

    * Neither the name of the copyright holder nor the names of its
        contributors may be used to endorse or promote products derived
        from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

    ---------------------------------------------------------------------------
    Note:
    Individual files contain the following tag instead of the full license text.

        SPDX-License-Identifier:    BSD-3-Clause

    This enables machine processing of license information based on the SPDX
    License Identifiers that are here available: http://spdx.org/licenses/

## PyInstaller

### License

    ================================
    The PyInstaller licensing terms
    ================================
    

    Copyright (c) 2010-2021, PyInstaller Development Team
    Copyright (c) 2005-2009, Giovanni Bajo
    Based on previous work under copyright (c) 2002 McMillan Enterprises, Inc.


    PyInstaller is licensed under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2 of the License,
    or (at your option) any later version.


    Bootloader Exception
    --------------------

    In addition to the permissions in the GNU General Public License, the
    authors give you unlimited permission to link or embed compiled bootloader
    and related files into combinations with other programs, and to distribute
    those combinations without any restriction coming from the use of those
    files. (The General Public License restrictions do apply in other respects;
    for example, they cover modification of the files, and distribution when
    not linked into a combined executable.)
    
    
    Bootloader and Related Files
    ----------------------------

    Bootloader and related files are files which are embedded within the
    final executable. This includes files in directories:

    ./bootloader/
    ./PyInstaller/loader


    Run-time Hooks
    ----------------------------

    Run-time Hooks are a different kind of files embedded within the final
    executable. To ease moving them into a separate repository, or into the
    respective project, these file are now licensed under the Apache License,
    Version 2.0.

    Run-time Hooks are in the directory
    ./PyInstaller/hooks/rthooks

    
    About the PyInstaller Development Team
    --------------------------------------

    The PyInstaller Development Team is the set of contributors
    to the PyInstaller project. A full list with details is kept
    in the documentation directory, in the file
    ``doc/CREDITS.rst``.

    The core team that coordinates development on GitHub can be found here:
    https://github.com/pyinstaller/pyinstaller.  As of 2021, it consists of:

    * Hartmut Goebel
    * Jasper Harrison
    * Bryan Jones
    * Brenainn Woodsend
    * Rok Mandeljc

    Our Copyright Policy
    --------------------

    PyInstaller uses a shared copyright model. Each contributor maintains copyright
    over their contributions to PyInstaller. But, it is important to note that these
    contributions are typically only changes to the repositories. Thus,
    the PyInstaller source code, in its entirety is not the copyright of any single
    person or institution.  Instead, it is the collective copyright of the entire
    PyInstaller Development Team.  If individual contributors want to maintain
    a record of what changes/contributions they have specific copyright on, they
    should indicate their copyright in the commit message of the change, when they
    commit the change to the PyInstaller repository.

    With this in mind, the following banner should be used in any source code file
    to indicate the copyright and license terms:


    #-----------------------------------------------------------------------------
    # Copyright (c) 2005-2021, PyInstaller Development Team.
    #
    # Distributed under the terms of the GNU General Public License (version 2
    # or later) with exception for distributing the bootloader.
    #
    # The full license is in the file COPYING.txt, distributed with this software.
    #
    # SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
    #-----------------------------------------------------------------------------


    For run-time hooks, the following banner should be used:

    #-----------------------------------------------------------------------------
    # Copyright (c) 2005-2021, PyInstaller Development Team.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    #
    # The full license is in the file COPYING.txt, distributed with this software.
    #
    # SPDX-License-Identifier: Apache-2.0
    #-----------------------------------------------------------------------------


    ================================
    GNU General Public License
    ================================

    https://gnu.org/licenses/gpl-2.0.html


                GNU GENERAL PUBLIC LICENSE
                Version 2, June 1991

    Copyright (C) 1989, 1991 Free Software Foundation, Inc.
    51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
    Everyone is permitted to copy and distribute verbatim copies
    of this license document, but changing it is not allowed.

                    Preamble

    The licenses for most software are designed to take away your
    freedom to share and change it.  By contrast, the GNU General Public
    License is intended to guarantee your freedom to share and change free
    software--to make sure the software is free for all its users.  This
    General Public License applies to most of the Free Software
    Foundation's software and to any other program whose authors commit to
    using it.  (Some other Free Software Foundation software is covered by
    the GNU Library General Public License instead.)  You can apply it to
    your programs, too.

    When we speak of free software, we are referring to freedom, not
    price.  Our General Public Licenses are designed to make sure that you
    have the freedom to distribute copies of free software (and charge for
    this service if you wish), that you receive source code or can get it
    if you want it, that you can change the software or use pieces of it
    in new free programs; and that you know you can do these things.

    To protect your rights, we need to make restrictions that forbid
    anyone to deny you these rights or to ask you to surrender the rights.
    These restrictions translate to certain responsibilities for you if you
    distribute copies of the software, or if you modify it.

    For example, if you distribute copies of such a program, whether
    gratis or for a fee, you must give the recipients all the rights that
    you have.  You must make sure that they, too, receive or can get the
    source code.  And you must show them these terms so they know their
    rights.

    We protect your rights with two steps: (1) copyright the software, and
    (2) offer you this license which gives you legal permission to copy,
    distribute and/or modify the software.

    Also, for each author's protection and ours, we want to make certain
    that everyone understands that there is no warranty for this free
    software.  If the software is modified by someone else and passed on, we
    want its recipients to know that what they have is not the original, so
    that any problems introduced by others will not reflect on the original
    authors' reputations.

    Finally, any free program is threatened constantly by software
    patents.  We wish to avoid the danger that redistributors of a free
    program will individually obtain patent licenses, in effect making the
    program proprietary.  To prevent this, we have made it clear that any
    patent must be licensed for everyone's free use or not licensed at all.

    The precise terms and conditions for copying, distribution and
    modification follow.

                GNU GENERAL PUBLIC LICENSE
    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

    0. This License applies to any program or other work which contains
    a notice placed by the copyright holder saying it may be distributed
    under the terms of this General Public License.  The "Program", below,
    refers to any such program or work, and a "work based on the Program"
    means either the Program or any derivative work under copyright law:
    that is to say, a work containing the Program or a portion of it,
    either verbatim or with modifications and/or translated into another
    language.  (Hereinafter, translation is included without limitation in
    the term "modification".)  Each licensee is addressed as "you".

    Activities other than copying, distribution and modification are not
    covered by this License; they are outside its scope.  The act of
    running the Program is not restricted, and the output from the Program
    is covered only if its contents constitute a work based on the
    Program (independent of having been made by running the Program).
    Whether that is true depends on what the Program does.

    1. You may copy and distribute verbatim copies of the Program's
    source code as you receive it, in any medium, provided that you
    conspicuously and appropriately publish on each copy an appropriate
    copyright notice and disclaimer of warranty; keep intact all the
    notices that refer to this License and to the absence of any warranty;
    and give any other recipients of the Program a copy of this License
    along with the Program.

    You may charge a fee for the physical act of transferring a copy, and
    you may at your option offer warranty protection in exchange for a fee.

    2. You may modify your copy or copies of the Program or any portion
    of it, thus forming a work based on the Program, and copy and
    distribute such modifications or work under the terms of Section 1
    above, provided that you also meet all of these conditions:

        a) You must cause the modified files to carry prominent notices
        stating that you changed the files and the date of any change.

        b) You must cause any work that you distribute or publish, that in
        whole or in part contains or is derived from the Program or any
        part thereof, to be licensed as a whole at no charge to all third
        parties under the terms of this License.

        c) If the modified program normally reads commands interactively
        when run, you must cause it, when started running for such
        interactive use in the most ordinary way, to print or display an
        announcement including an appropriate copyright notice and a
        notice that there is no warranty (or else, saying that you provide
        a warranty) and that users may redistribute the program under
        these conditions, and telling the user how to view a copy of this
        License.  (Exception: if the Program itself is interactive but
        does not normally print such an announcement, your work based on
        the Program is not required to print an announcement.)

    These requirements apply to the modified work as a whole.  If
    identifiable sections of that work are not derived from the Program,
    and can be reasonably considered independent and separate works in
    themselves, then this License, and its terms, do not apply to those
    sections when you distribute them as separate works.  But when you
    distribute the same sections as part of a whole which is a work based
    on the Program, the distribution of the whole must be on the terms of
    this License, whose permissions for other licensees extend to the
    entire whole, and thus to each and every part regardless of who wrote it.

    Thus, it is not the intent of this section to claim rights or contest
    your rights to work written entirely by you; rather, the intent is to
    exercise the right to control the distribution of derivative or
    collective works based on the Program.

    In addition, mere aggregation of another work not based on the Program
    with the Program (or with a work based on the Program) on a volume of
    a storage or distribution medium does not bring the other work under
    the scope of this License.

    3. You may copy and distribute the Program (or a work based on it,
    under Section 2) in object code or executable form under the terms of
    Sections 1 and 2 above provided that you also do one of the following:

        a) Accompany it with the complete corresponding machine-readable
        source code, which must be distributed under the terms of Sections
        1 and 2 above on a medium customarily used for software interchange; or,

        b) Accompany it with a written offer, valid for at least three
        years, to give any third party, for a charge no more than your
        cost of physically performing source distribution, a complete
        machine-readable copy of the corresponding source code, to be
        distributed under the terms of Sections 1 and 2 above on a medium
        customarily used for software interchange; or,

        c) Accompany it with the information you received as to the offer
        to distribute corresponding source code.  (This alternative is
        allowed only for noncommercial distribution and only if you
        received the program in object code or executable form with such
        an offer, in accord with Subsection b above.)

    The source code for a work means the preferred form of the work for
    making modifications to it.  For an executable work, complete source
    code means all the source code for all modules it contains, plus any
    associated interface definition files, plus the scripts used to
    control compilation and installation of the executable.  However, as a
    special exception, the source code distributed need not include
    anything that is normally distributed (in either source or binary
    form) with the major components (compiler, kernel, and so on) of the
    operating system on which the executable runs, unless that component
    itself accompanies the executable.

    If distribution of executable or object code is made by offering
    access to copy from a designated place, then offering equivalent
    access to copy the source code from the same place counts as
    distribution of the source code, even though third parties are not
    compelled to copy the source along with the object code.

    4. You may not copy, modify, sublicense, or distribute the Program
    except as expressly provided under this License.  Any attempt
    otherwise to copy, modify, sublicense or distribute the Program is
    void, and will automatically terminate your rights under this License.
    However, parties who have received copies, or rights, from you under
    this License will not have their licenses terminated so long as such
    parties remain in full compliance.

    5. You are not required to accept this License, since you have not
    signed it.  However, nothing else grants you permission to modify or
    distribute the Program or its derivative works.  These actions are
    prohibited by law if you do not accept this License.  Therefore, by
    modifying or distributing the Program (or any work based on the
    Program), you indicate your acceptance of this License to do so, and
    all its terms and conditions for copying, distributing or modifying
    the Program or works based on it.

    6. Each time you redistribute the Program (or any work based on the
    Program), the recipient automatically receives a license from the
    original licensor to copy, distribute or modify the Program subject to
    these terms and conditions.  You may not impose any further
    restrictions on the recipients' exercise of the rights granted herein.
    You are not responsible for enforcing compliance by third parties to
    this License.

    7. If, as a consequence of a court judgment or allegation of patent
    infringement or for any other reason (not limited to patent issues),
    conditions are imposed on you (whether by court order, agreement or
    otherwise) that contradict the conditions of this License, they do not
    excuse you from the conditions of this License.  If you cannot
    distribute so as to satisfy simultaneously your obligations under this
    License and any other pertinent obligations, then as a consequence you
    may not distribute the Program at all.  For example, if a patent
    license would not permit royalty-free redistribution of the Program by
    all those who receive copies directly or indirectly through you, then
    the only way you could satisfy both it and this License would be to
    refrain entirely from distribution of the Program.

    If any portion of this section is held invalid or unenforceable under
    any particular circumstance, the balance of the section is intended to
    apply and the section as a whole is intended to apply in other
    circumstances.

    It is not the purpose of this section to induce you to infringe any
    patents or other property right claims or to contest validity of any
    such claims; this section has the sole purpose of protecting the
    integrity of the free software distribution system, which is
    implemented by public license practices.  Many people have made
    generous contributions to the wide range of software distributed
    through that system in reliance on consistent application of that
    system; it is up to the author/donor to decide if he or she is willing
    to distribute software through any other system and a licensee cannot
    impose that choice.

    This section is intended to make thoroughly clear what is believed to
    be a consequence of the rest of this License.

    8. If the distribution and/or use of the Program is restricted in
    certain countries either by patents or by copyrighted interfaces, the
    original copyright holder who places the Program under this License
    may add an explicit geographical distribution limitation excluding
    those countries, so that distribution is permitted only in or among
    countries not thus excluded.  In such case, this License incorporates
    the limitation as if written in the body of this License.

    9. The Free Software Foundation may publish revised and/or new versions
    of the General Public License from time to time.  Such new versions will
    be similar in spirit to the present version, but may differ in detail to
    address new problems or concerns.

    Each version is given a distinguishing version number.  If the Program
    specifies a version number of this License which applies to it and "any
    later version", you have the option of following the terms and conditions
    either of that version or of any later version published by the Free
    Software Foundation.  If the Program does not specify a version number of
    this License, you may choose any version ever published by the Free Software
    Foundation.

    10. If you wish to incorporate parts of the Program into other free
    programs whose distribution conditions are different, write to the author
    to ask for permission.  For software which is copyrighted by the Free
    Software Foundation, write to the Free Software Foundation; we sometimes
    make exceptions for this.  Our decision will be guided by the two goals
    of preserving the free status of all derivatives of our free software and
    of promoting the sharing and reuse of software generally.

                    NO WARRANTY

    11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
    FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
    OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
    PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
    OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
    TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
    PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
    REPAIR OR CORRECTION.

    12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
    WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
    REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
    INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
    OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
    TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
    YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
    PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGES.

                END OF TERMS AND CONDITIONS

    ================================
    Apache License 2.0
    ================================

                                    Apache License
                            Version 2.0, January 2004
                            http://www.apache.org/licenses/

    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

    1. Definitions.

        "License" shall mean the terms and conditions for use, reproduction,
        and distribution as defined by Sections 1 through 9 of this document.

        "Licensor" shall mean the copyright owner or entity authorized by
        the copyright owner that is granting the License.

        "Legal Entity" shall mean the union of the acting entity and all
        other entities that control, are controlled by, or are under common
        control with that entity. For the purposes of this definition,
        "control" means (i) the power, direct or indirect, to cause the
        direction or management of such entity, whether by contract or
        otherwise, or (ii) ownership of fifty percent (50%) or more of the
        outstanding shares, or (iii) beneficial ownership of such entity.

        "You" (or "Your") shall mean an individual or Legal Entity
        exercising permissions granted by this License.

        "Source" form shall mean the preferred form for making modifications,
        including but not limited to software source code, documentation
        source, and configuration files.

        "Object" form shall mean any form resulting from mechanical
        transformation or translation of a Source form, including but
        not limited to compiled object code, generated documentation,
        and conversions to other media types.

        "Work" shall mean the work of authorship, whether in Source or
        Object form, made available under the License, as indicated by a
        copyright notice that is included in or attached to the work
        (an example is provided in the Appendix below).

        "Derivative Works" shall mean any work, whether in Source or Object
        form, that is based on (or derived from) the Work and for which the
        editorial revisions, annotations, elaborations, or other modifications
        represent, as a whole, an original work of authorship. For the purposes
        of this License, Derivative Works shall not include works that remain
        separable from, or merely link (or bind by name) to the interfaces of,
        the Work and Derivative Works thereof.

        "Contribution" shall mean any work of authorship, including
        the original version of the Work and any modifications or additions
        to that Work or Derivative Works thereof, that is intentionally
        submitted to Licensor for inclusion in the Work by the copyright owner
        or by an individual or Legal Entity authorized to submit on behalf of
        the copyright owner. For the purposes of this definition, "submitted"
        means any form of electronic, verbal, or written communication sent
        to the Licensor or its representatives, including but not limited to
        communication on electronic mailing lists, source code control systems,
        and issue tracking systems that are managed by, or on behalf of, the
        Licensor for the purpose of discussing and improving the Work, but
        excluding communication that is conspicuously marked or otherwise
        designated in writing by the copyright owner as "Not a Contribution."

        "Contributor" shall mean Licensor and any individual or Legal Entity
        on behalf of whom a Contribution has been received by Licensor and
        subsequently incorporated within the Work.

    2. Grant of Copyright License. Subject to the terms and conditions of
        this License, each Contributor hereby grants to You a perpetual,
        worldwide, non-exclusive, no-charge, royalty-free, irrevocable
        copyright license to reproduce, prepare Derivative Works of,
        publicly display, publicly perform, sublicense, and distribute the
        Work and such Derivative Works in Source or Object form.

    3. Grant of Patent License. Subject to the terms and conditions of
        this License, each Contributor hereby grants to You a perpetual,
        worldwide, non-exclusive, no-charge, royalty-free, irrevocable
        (except as stated in this section) patent license to make, have made,
        use, offer to sell, sell, import, and otherwise transfer the Work,
        where such license applies only to those patent claims licensable
        by such Contributor that are necessarily infringed by their
        Contribution(s) alone or by combination of their Contribution(s)
        with the Work to which such Contribution(s) was submitted. If You
        institute patent litigation against any entity (including a
        cross-claim or counterclaim in a lawsuit) alleging that the Work
        or a Contribution incorporated within the Work constitutes direct
        or contributory patent infringement, then any patent licenses
        granted to You under this License for that Work shall terminate
        as of the date such litigation is filed.

    4. Redistribution. You may reproduce and distribute copies of the
        Work or Derivative Works thereof in any medium, with or without
        modifications, and in Source or Object form, provided that You
        meet the following conditions:

        (a) You must give any other recipients of the Work or
            Derivative Works a copy of this License; and

        (b) You must cause any modified files to carry prominent notices
            stating that You changed the files; and

        (c) You must retain, in the Source form of any Derivative Works
            that You distribute, all copyright, patent, trademark, and
            attribution notices from the Source form of the Work,
            excluding those notices that do not pertain to any part of
            the Derivative Works; and

        (d) If the Work includes a "NOTICE" text file as part of its
            distribution, then any Derivative Works that You distribute must
            include a readable copy of the attribution notices contained
            within such NOTICE file, excluding those notices that do not
            pertain to any part of the Derivative Works, in at least one
            of the following places: within a NOTICE text file distributed
            as part of the Derivative Works; within the Source form or
            documentation, if provided along with the Derivative Works; or,
            within a display generated by the Derivative Works, if and
            wherever such third-party notices normally appear. The contents
            of the NOTICE file are for informational purposes only and
            do not modify the License. You may add Your own attribution
            notices within Derivative Works that You distribute, alongside
            or as an addendum to the NOTICE text from the Work, provided
            that such additional attribution notices cannot be construed
            as modifying the License.

        You may add Your own copyright statement to Your modifications and
        may provide additional or different license terms and conditions
        for use, reproduction, or distribution of Your modifications, or
        for any such Derivative Works as a whole, provided Your use,
        reproduction, and distribution of the Work otherwise complies with
        the conditions stated in this License.

    5. Submission of Contributions. Unless You explicitly state otherwise,
        any Contribution intentionally submitted for inclusion in the Work
        by You to the Licensor shall be under the terms and conditions of
        this License, without any additional terms or conditions.
        Notwithstanding the above, nothing herein shall supersede or modify
        the terms of any separate license agreement you may have executed
        with Licensor regarding such Contributions.

    6. Trademarks. This License does not grant permission to use the trade
        names, trademarks, service marks, or product names of the Licensor,
        except as required for reasonable and customary use in describing the
        origin of the Work and reproducing the content of the NOTICE file.

    7. Disclaimer of Warranty. Unless required by applicable law or
        agreed to in writing, Licensor provides the Work (and each
        Contributor provides its Contributions) on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
        implied, including, without limitation, any warranties or conditions
        of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
        PARTICULAR PURPOSE. You are solely responsible for determining the
        appropriateness of using or redistributing the Work and assume any
        risks associated with Your exercise of permissions under this License.

    8. Limitation of Liability. In no event and under no legal theory,
        whether in tort (including negligence), contract, or otherwise,
        unless required by applicable law (such as deliberate and grossly
        negligent acts) or agreed to in writing, shall any Contributor be
        liable to You for damages, including any direct, indirect, special,
        incidental, or consequential damages of any character arising as a
        result of this License or out of the use or inability to use the
        Work (including but not limited to damages for loss of goodwill,
        work stoppage, computer failure or malfunction, or any and all
        other commercial damages or losses), even if such Contributor
        has been advised of the possibility of such damages.

    9. Accepting Warranty or Additional Liability. While redistributing
        the Work or Derivative Works thereof, You may choose to offer,
        and charge a fee for, acceptance of support, warranty, indemnity,
        or other liability obligations and/or rights consistent with this
        License. However, in accepting such obligations, You may act only
        on Your own behalf and on Your sole responsibility, not on behalf
        of any other Contributor, and only if You agree to indemnify,
        defend, and hold each Contributor harmless for any liability
        incurred by, or claims asserted against, such Contributor by reason
        of your accepting any such warranty or additional liability.

    END OF TERMS AND CONDITIONS

    APPENDIX: How to apply the Apache License to your work.

        To apply the Apache License to your work, attach the following
        boilerplate notice, with the fields enclosed by brackets "[]"
        replaced with your own identifying information. (Don't include
        the brackets!)  The text should be enclosed in the appropriate
        comment syntax for the file format. We also recommend that a
        file or class name and description of purpose be included on the
        same "printed page" as the copyright notice for easier
        identification within third-party archives.

    Copyright [yyyy] [name of copyright owner]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.