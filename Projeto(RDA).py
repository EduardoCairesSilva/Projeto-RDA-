NomeRDA = ('LAMMAS', 'MABON', 'SAMHAIN', 'YULE', 'IMBOLC',
           'OSTARA', 'BELTANE', 'LITHA')
NomeRDA2 = ('IMBOLC', 'OSTARA', 'BELTANE', 'LITHA', 'LAMMAS',
            'MABON', 'SAMHAIN', 'YULE')
print('''\33[1;33m[PT] PT-BR
[US] EN-US''')
idioma = str(input('Escolha um idioma: ')).strip().upper()
print('''\33[1;33m[HS] HEMISFÉRIO SUL
[HN] HEMISFÉRIO NORTE''')
local = str(input('Qual hemisfério você quer ver?: \33[m')).strip().upper()
while True:
    if idioma == 'PT':
        if local == 'HS':
            print('\33[1;31mESCOLHA:')
            print('LAMMAS,', 'MABON,', 'SAMHAIN,', 'YULE,')
            print('-'*30)
            print('IMBOLC,', 'OSTARA,', 'BELTANE,', 'LITHA,' ' TODAS.\33[m')
            nome = str(input('\33[1;35mEscolha uma data: ')).strip().upper()
            if nome == 'LAMMAS':
                print(f'''{nome} >>>>>>>> DATA DE INICIO: 01 DE FEVEREIRO
                DATA DO TÉRMINO: 28 DE FEVEREIRO
                DESCRIÇÃO: Festa da colheita, é celebrada em 1° de fevereiro.
                Pronunciado como lammas, essa é uma festividade que homenageia
                o deus Lugh. Ele celebra o inicio do período de colheita dos
                grãos. Este é o primerio festival da colheita, quando as
                plantas deixam cair suas sementes para garantir o ciclo.''')
            elif nome == 'MABON':
                print(f'''{nome} >>>>>>>>> DATA DE INICIO: 20 DE MARÇO
                DATA DE TÉRMINO: 23 DE MARÇO
                DESCRIÇÃO: Acontece no dia 20 de março. Mabon é um momento
                de ação de graças que celebra a segunda colheita, os dias e
                as noites são novamente iguais, mas a noite segue crescendo
                cada vez mais. Também é conhecida como Alban Elfed
                (a Luz da Água).
                ESTAÇÃO: EQUINÓCIO DE OUTONO,''')
            elif nome == 'SAMHAIN':
                print(f'''{nome} >>>>>>> DIA DE INICIO: 30 DE ABRIL
                DIA DO TÉRMINO: 31 DE ABRIL
                DESCRIÇÃO: É o ano novo celta, acontece em 30 de abril.
                Pronunciado Sou-Em, representa a colheita final que antecede
                um longo inverno. É hora de homenagear os nossos antepassados
                e abraçar a metade mais escura do ano. Samhain também
                marcar o início do Ano Novo em muitas tradições pagãs.''')
            elif nome == 'YULE':
                print(f'''{nome} >>>>>>>>>> DIA DE INICIO: 20 DE JUNHO
                DIA DO TÉRMINO: 23 DE JUNHO
                DESCRIÇÃO: Ocorre em 20 de junho. Yule marca o dia
                mais curto do ano. A partir de agora, os dias se tornam
                mais longos e comemoramos o retorno do sol à terra.
                A data também é conhecida como Alban Altha.
                ESTAÇÃO: SOLSTÍCIO DE INVERNO''')
            elif nome == 'IMBOLC':
                print(f'''{nome} >>>>>>>> DIA DE INICIO: 1 DE AGOSTO
                DIA DO TÉRMINO: 2 DE AGOSTO
                DESCRIÇÃO: Festa do fogo, do Sol e da luz
                é celebrada em 1° de agosto. Imbolc é um festival que,
                em muitas tradições, celebra a deusa celta Brigid.
                A data marca o intermédio entre o inverno e a primavera,
                firmando-se como um festival de purificação, luz, fertilidade
                e novos começos.''')
            elif nome == 'OSTARA':
                print(f'''{nome} >>>>>>>> DIA DE INICIO: 20 DE SETEMBRO
                DIA DO TÉRMINO: 23 DE SETEMBRO
                DESCRIÇÃO: Festa da fertilidade, acontece em 20 de setembro.
                Ostara é um momento para se preparar para o inicio de uma
                nova vida. As hotas do dia e da noite são iguais, e a luz
                ultrapassa a escuridão. Também é conhecida como Alban Eilir.
                ESTAÇÃO: EQUINÓCIO DE PRIMAVERA.''')
            elif nome == 'BELTANE':
                print(f'''{nome} >>>>>>> DIA DE INICIO: 31 DE OUTUBRO
                DIA DO TÉRMINO: 1 DE NOVEMBRO
                DESCRIÇÃO: Festa da primavera, é celebrada em 31 de outubro.
                Beltane é uma festividade que honra a fertilidade da terra.
                Consiste em um tempo de luxúria, paixão, fogo e abundância.''')
            elif nome == 'LITHA':
                print(f'''{nome} >>>>>>>>> DIA DE INICIO: 20 DE DEZEMBRO
                DIA DO TÉRMINO: 23 DE DEZEMBRO
                DESCRIÇÃO: Ocorre em 20 de dezembro.
                Litha marca o dia mais longo do ano. É uma celebração do
                triunfo da luz sobre as trevas, e da beleza abundante que
                a luz proporciona às nossas vidas. Tambpem é conhecida como
                Alban Hefin.
                ESTAÇÃO: SOLSTÍCIO DE VERÃO.\33[m''')
            elif nome == 'TODAS':
                print('''LAMMAS >>>>>>>> DATA DE INICIO: 01 DE FEVEREIRO
                DATA DO TÉRMINO: 28 DE FEVEREIRO
                DESCRIÇÃO: Festa da colheita, é celebrada em 1° de fevereiro.
                Pronunciado como lammas, essa é uma festividade que homenageia
                o deus Lugh. Ele celebra o inicio do período de colheita dos
                grãos. Este é o primerio festival da colheita, quando as
                plantas deixam cair suas sementes para garantir o ciclo.''')
                print('-=-'*40)
                print('''MABON >>>>>>>>> DATA DE INICIO: 20 DE MARÇO,
                DATA DE TÉRMINO: 23 DE MARÇO
                DESCRIÇÃO: Acontece no dia 20 de março. Mabon é um momento
                de ação de graças que celebra a segunda colheita, os dias e
                as noites são novamente iguais, mas a noite segue crescendo
                cada vez mais. Também é conhecida como Alban Elfed
                (a Luz da Água).
                ESTAÇÃO: EQUINÓCIO DE OUTONO,''')
                print('-=-'*40)
                print('''SAMHAIN >>>>>>> DIA DE INICIO: 30 DE ABRIL
                DIA DO TÉRMINO: 31 DE ABRIL
                DESCRIÇÃO: É o ano novo celta, acontece em 30 de abril.
                Pronunciado Sou-Em, representa a colheita final que antecede
                um longo inverno. É hora de homenagear os nossos antepassados
                e abraçar a metade mais escura do ano. Samhain também
                marcar o início do Ano Novo em muitas tradições pagãs.''')
                print('-=-'*40)
                print('''YULE >>>>>>>>>> DIA DE INICIO: 20 DE JUNHO
                DIA DO TÉRMINO: 23 DE JUNHO
                DESCRIÇÃO: Ocorre em 20 de junho. Yule marca o dia
                mais curto do ano. A partir de agora, os dias se tornam
                mais longos e comemoramos o retorno do sol à terra.
                A data também é conhecida como Alban Altha.
                ESTAÇÃO: SOLSTÍCIO DE INVERNO''')
                print('-=-'*40)
                print('''IMBOLC >>>>>>>> DIA DE INICIO: 1 DE AGOSTO
                DIA DO TÉRMINO: 2 DE AGOSTO
                DESCRIÇÃO: Festa do fogo, do Sol e da luz
                é celebrada em 1° de agosto. Imbolc é um festival que,
                em muitas tradições, celebra a deusa celta Brigid.
                A data marca o intermédio entre o inverno e a primavera,
                firmando-se como um festival de purificação, luz, fertilidade
                e novos começos.''')
                print('-=-'*40)
                print('''OSTARA >>>>>>>> DIA DE INICIO: 20 DE SETEMBRO
                DIA DO TÉRMINO: 23 DE SETEMBRO
                DESCRIÇÃO: Festa da fertilidade, acontece em 20 de setembro.
                Ostara é um momento para se preparar para o inicio de uma
                nova vida. As hotas do dia e da noite são iguais, e a luz
                ultrapassa a escuridão. Também é conhecida como Alban Eilir.
                ESTAÇÃO: EQUINÓCIO DE PRIMAVERA.''')
                print('-=-'*40)
                print('''BELTANE >>>>>>> DIA DE INICIO: 31 DE OUTUBRO
                DIA DO TÉRMINO: 1 DE NOVEMBRO
                DESCRIÇÃO: Festa da primavera, é celebrada em 31 de outubro.
                Beltane é uma festividade que honra a fertilidade da terra.
                Consiste em um tempo de luxúria, paixão, fogo e abundância.''')
                print('-=-'*40)
                print('''LITHA >>>>>>>>> DIA DE INICIO: 20 DE DEZEMBRO
                DIA DO TÉRMINO: 23 DE DEZEMBRO
                DESCRIÇÃO: Ocorre em 20 de dezembro.
                Litha marca o dia mais longo do ano. É uma celebração do
                triunfo da luz sobre as trevas, e da beleza abundante que a luz
                proporciona às nossas vidas. Tambpem é conhecida como
                Alban Hefin.
                ESTAÇÃO: SOLSTÍCIO DE VERÃO.\33[m''')
            elif nome != NomeRDA:
                break
            resp1 = str(input('\33[1;35mContinuar? {S/N}:')).strip().upper()[0]
            if resp1 in 'N':
                break
            elif resp1 not in 'SN':
                break
        if local == 'HN':
            print('\33[1;31mESCOLHA:')
            print('IMBOLC,', 'OSTARA,', 'BELTANE,', 'LITHA,')
            print('-'*30)
            print('LAMMAS,', 'MABON,', 'SAMHAIN,', 'YULE,', ' TODAS.\33[m')
            nome = str(input('\33[1;35mEscolha uma data: ')).strip().upper()
            if nome == 'IMBOLC':
                print(f'''{nome} >>>>>>>> DIA DE INICIO: 1 DE FEVEREIRO
                DIA DO TÉRMINO: 2 DE FEVEREIRO
                DESCRIÇÃO: Festa do fogo, do Sol e da luz
                é celebrada em 1° de fevereiro. Imbolc é um festival que,
                em muitas tradições, celebra a deusa celta Brigid.
                A data marca o intermédio entre o inverno e a primavera,
                firmando-se como um festival de purificação, luz, fertilidade
                e novos começos.''')
            elif nome == 'OSTARA':
                print(f'''{nome} >>>>>>>> DIA DE INICIO: 17 DE MARÇO
                DIA DO TÉRMINO: 22 DE MARÇO
                DESCRIÇÃO: Festa da fertilidade, acontece em 17 de março.
                Ostara é um momento para se preparar para o inicio de uma
                nova vida. As hotas do dia e da noite são iguais, e a luz
                ultrapassa a escuridão. Também é conhecida como Alban Eilir.
                ESTAÇÃO: EQUINÓCIO DE PRIMAVERA''')
            elif nome == 'BELTANE':
                print(f'''{nome} >>>>>>> DIA DE INICIO: 30 DE ABRIL
                DIA DO TÉRMINO: 30 DE ABRIL
                DESCRIÇÃO: Festa da primavera, é celebrada em 30 de abril.
                Beltane é uma festividade que honra a fertilidade da terra.
                Consiste em um tempo de luxúria, paixão, fogo e abundância.''')
            elif nome == 'LITHA':
                print(f'''{nome} >>>>>>>>> DIA DE INICIO: 21 DE JUNHO
                DIA DO TÉRMINO: 01 DE JULHO
                DESCRIÇÃO: Ocorre em 21 de junho.
                Litha marca o dia mais longo do ano. É uma celebração do
                triunfo da luz sobre as trevas, e da beleza abundante que
                a luz proporciona às nossas vidas. Tambpem é conhecida como
                Alban Hefin.
                ESTAÇÃO: SOLSTÍCIO DE VERÃO''')
            elif nome == 'LAMMAS':
                print(f'''{nome} >>>>>>>> DATA DE INICIO: 1 DE AGOSTO
                DATA DO TÉRMINO: 2 DE AGOSTO
                DESCRIÇÃO: Festa da colheita, é celebrada em 1° de agosto.
                Pronunciado como lammas, essa é uma festividade que homenageia
                o deus Lugh. Ele celebra o inicio do período de colheita dos
                grãos. Este é o primerio festival da colheita, quando as
                plantas deixam cair suas sementes para garantir o ciclo.''')
            elif nome == 'MABON':
                print(f'''{nome} >>>>>>>>> DATA DE INICIO: 21 DE SETEMBRO
                DATA DE TÉRMINO: 29 DE SETEMBRO
                DESCRIÇÃO: Acontece no dia 21 de setembro. Mabon é um momento
                de ação de graças que celebra a segunda colheita, os dias e
                as noites são novamente iguais, mas a noite segue crescendo
                cada vez mais. Também é conhecida como Alban Elfed
                (a Luz da Água).
                ESTAÇÃO: EQUINÓCIO DE OUTONO,''')
            elif nome == 'SAMHAIN':
                print(f'''{nome} >>>>>>> DIA DE INICIO: 31 DE OUTUBRO
                DIA DO TÉRMINO: 31 DE OUTUBRO
                DESCRIÇÃO: É o ano novo celta, acontece em 31 de outubro.
                Pronunciado Sou-Em, representa a colheita final que antecede
                um longo inverno. É hora de homenagear os nossos antepassados
                e abraçar a metade mais escura do ano. Samhain também
                marcar o início do Ano Novo em muitas tradições pagãs.''')
            elif nome == 'YULE':
                print(f'''{nome} >>>>>>>>>> DIA DE INICIO: 21 DE DEZEMBRO
                DIA DO TÉRMINO: 23 DE DEZEMBRO
                DESCRIÇÃO: Ocorre em 21 de dezembro. Yule marca o dia
                mais curto do ano. A partir de agora, os dias se tornam
                mais longos e comemoramos o retorno do sol à terra.
                A data também é conhecida como Alban Altha.
                ESTAÇÃO: SOLSTÍCIO DE INVERNO''')
            elif nome == 'TODAS':
                print('''IMBOLC >>>>>>>> DIA DE INICIO: 1 DE FEVEREIRO
                DIA DO TÉRMINO: 2 DE FEVEREIRO
                DESCRIÇÃO: Festa do fogo, do Sol e da luz
                é celebrada em 1° de fevereiro. Imbolc é um festival que,
                em muitas tradições, celebra a deusa celta Brigid.
                A data marca o intermédio entre o inverno e a primavera,
                firmando-se como um festival de purificação, luz, fertilidade
                e novos começos.''')
                print('-=-'*40)
                print('''OSTARA >>>>>>>> DIA DE INICIO: 17 DE MARÇO
                DIA DO TÉRMINO: 22 DE MARÇO
                DESCRIÇÃO: Festa da fertilidade, acontece em 17 de março.
                Ostara é um momento para se preparar para o inicio de uma
                nova vida. As horas do dia e da noite são iguais, e a luz
                ultrapassa a escuridão. Também é conhecida como Alban Eilir.
                ESTAÇÃO: EQUINÓCIO DE PRIMAVERA''')
                print('-=-'*40)
                print('''BELTANE >>>>>>> DIA DE INICIO: 30 DE ABRIL
                DIA DO TÉRMINO: 30 DE ABRIL
                DESCRIÇÃO: Festa da primavera, é celebrada em 30 de abril.
                Beltane é uma festividade que honra a fertilidade da terra.
                Consiste em um tempo de luxúria, paixão, fogo e abundância.''')
                print('-=-'*40)
                print('''LITHA >>>>>>>>> DIA DE INICIO: 21 DE JUNHO
                DIA DO TÉRMINO: 01 DE JULHO
                DESCRIÇÃO: Ocorre em 21 de junho.
                Litha marca o dia mais longo do ano. É uma celebração do
                triunfo da luz sobre as trevas, e da beleza abundante que
                a luz proporciona às nossas vidas. Também é conhecida como
                Alban Hefin.
                ESTAÇÃO: SOLSTÍCIO DE VERÃO''')
                print('-=-'*40)
                print('''LAMMAS >>>>>>>> DATA DE INICIO: 1 DE AGOSTO
                DATA DO TÉRMINO: 2 DE AGOSTO
                DESCRIÇÃO: Festa da colheita, é celebrada em 1° de agosto.
                Pronunciado como lammas, essa é uma festividade que homenageia
                o deus Lugh. Ele celebra o inicio do período de colheita dos
                grãos. Este é o primerio festival da colheita, quando as
                plantas deixam cair suas sementes para garantir o ciclo.''')
                print('-=-'*40)
                print('''MABON >>>>>>>>> DATA DE INICIO: 21 DE SETEMBRO
                DATA DE TÉRMINO: 29 DE SETEMBRO
                DESCRIÇÃO: Acontece no dia 21 de setembro. Mabon é um momento
                de ação de graças que celebra a segunda colheita, os dias e
                as noites são novamente iguais, mas a noite segue crescendo
                cada vez mais. Também é conhecida como Alban Elfed
                (a Luz da Água).
                ESTAÇÃO: EQUINÓCIO DE OUTONO,''')
                print('-=-'*40)
                print('''SAMHAIN >>>>>>> DIA DE INICIO: 31 DE OUTUBRO
                DIA DO TÉRMINO: 31 DE OUTUBRO
                DESCRIÇÃO: É o ano novo celta, acontece em 31 de outubro.
                Pronunciado Sou-Em, representa a colheita final que antecede
                um longo inverno. É hora de homenagear os nossos antepassados
                e abraçar a metade mais escura do ano. Samhain também
                marcar o início do Ano Novo em muitas tradições pagãs.''')
                print('-=-'*40)
                print('''YULE >>>>>>>>>> DIA DE INICIO: 21 DE DEZEMBRO
                DIA DO TÉRMINO: 23 DE DEZEMBRO
                DESCRIÇÃO: Ocorre em 21 de dezembro. Yule marca o dia
                mais curto do ano. A partir de agora, os dias se tornam
                mais longos e comemoramos o retorno do sol à terra.
                A data também é conhecida como Alban Altha.
                ESTAÇÃO: SOLSTÍCIO DE INVERNO''')
            elif nome != NomeRDA2:
                break
            resp = str(input('Continuar? {S/N}: \33[m')).strip().upper()[0]
            if resp in 'N':
                break
            elif resp not in 'SN':
                break
    elif idioma == 'US':
        if local == 'HS':
            print('\33[1;31mCHOICE:')
            print('LAMMAS,', 'MABON,', 'SAMHAIN,', 'YULE,')
            print('-'*30)
            print('IMBOLC,', 'OSTARA,', 'BELTANE,', 'LITHA,', ' ALL.\33[m')
            name = str(input('\33[1;35mChoose a date: ')).strip().upper()
            if name == 'LAMMAS':
                print(f'''{name} >>>>>>>> START DATE: 01 FEBRUARY
                END DATE: FEBRUARY 28
                DESCRIPTION: Harvest Festival, celebrated on February 1st.
                Pronounced as lammas, this is a festival that honors the
                god Lugh. It celebrates the beginning of the grain harvest
                period. This is the first harvest festival, when the plants
                leave drop your seeds to ensure the cycle.''')
            elif name == 'MABON':
                print(f'''{name} >>>>>>>>> START DATE: MARCH 20,
                END DATE: MARCH 23
                DESCRIPTION: It takes place on March 20th. Mabon is a moment
                thanksgiving celebration that celebrates the second harvest,
                the days and the nights are the same again, but the night
                keeps growing increasingly. Also known as Alban Elfed
                (the Light of Water).
                SEASON: AUTUMN EQUINOX,''')
            elif name == 'SAMHAIN':
                print(f'''{name} >>>>>>> START DAY: APRIL 30
                END DAY: APRIL 31
                DESCRIPTION: It is the Celtic New Year, it takes place on
                April 30th. Pronounced Sou-Em, represents the final harvest
                that precedes a long winter. It's time to honor our ancestors
                and embrace the darkest half of the year. Samhain too
                mark the beginning of the New Year in many pagan
                traditions.''')
            elif name == 'YULE':
                print(f'''{name} >>>>>>>>>> START DAY: JUNE 20
                END DAY: JUNE 23
                DESCRIPTION: Occurs on June 20th. Yule marks the day
                shortest of the year. From now on, the days become
                longer and we celebrate the return of the sun to earth.
                The date is also known as Alban Altha.
                SEASON: WINTER SOLSTICE''')
            elif name == 'IMBOLC':
                print(f'''{name} >>>>>>>> START DAY: AUGUST 1
                END DAY: AUGUST 2
                DESCRIPTION: Feast of Fire, Sun and Light
                is celebrated on the 1st of August. Imbolc is a festival that,
                in many traditions, it celebrates the Celtic goddess Brigid.
                The date marks the middle between winter and spring,
                establishing itself as a festival of purification, light,
                fertility and new beginnings.''')
            elif name == 'OSTARA':
                print(f'''{name} >>>>>>>> START DAY: SEPTEMBER 20
                END DAY: SEPTEMBER 23
                DESCRIPTION: Feast of fertility, takes place on September 20th.
                Ostara is a time to prepare for the start of a
                new life. The hours of day and night are the same, and the
                light surpasses the darkness. It is also known as Alban Eilir.
                SEASON: SPRING EQUINOX.''')
            elif name == 'BELTANE':
                print(f'''{name} >>>>>>> START DAY: OCTOBER 31
                END DAY: NOVEMBER 1
                DESCRIPTION: Spring Festival is celebrated on October 31st.
                Beltane is a festival that honors the fertility of the land.
                It consists of a time of lust, passion, fire and abundance.''')
            elif name == 'LITHA':
                print(f'''{name} >>>>>>>>> START DAY: DECEMBER 20
                END DAY: DECEMBER 23
                DESCRIPTION: Occurs on December 20th.
                Litha marks the longest day of the year. It's a celebration of
                triumph of light over darkness, and of the abundant beauty that
                light gives to our lives. It is also known as
                Alban Hefin.
                SEASON: SUMMER SOLSTICE.\33[m''')
            elif name == 'ALL':
                print('''LAMMAS >>>>>>>> START DATE: 01 FEBRUARY
                END DATE: FEBRUARY 28
                DESCRIPTION: Harvest Festival, celebrated on February 1st.
                Pronounced as lammas, this is a festival that honors the
                god Lugh. It celebrates the beginning of the grain harvest
                period. This is the first harvest festival, when the plants
                leave drop your seeds to ensure the cycle.''')
                print('-=-'*40)
                print('''MABON >>>>>>>>> START DATE: MARCH 20,
                END DATE: MARCH 23
                DESCRIPTION: It takes place on March 20th. Mabon is a moment
                thanksgiving celebration that celebrates the second harvest,
                the days and the nights are the same again, but the night keeps
                growing increasingly. Also known as Alban Elfed
                (the Light of Water).
                SEASON: AUTUMN EQUINOX,''')
                print('-=-'*40)
                print('''SAMHAIN >>>>>>> START DAY: APRIL 30
                END DAY: APRIL 31
                DESCRIPTION: It is the Celtic New Year, it takes place on
                April 30th. Pronounced Sou-Em, represents the final harvest
                that precedes a long winter. It's time to honor our ancestors
                and embrace the darkest half of the year. Samhain too
                mark the beginning of the New Year in many Pagan
                traditions.''')
                print('-=-'*40)
                print('''YULE >>>>>>>>>> START DAY: JUNE 20
                END DAY: JUNE 23
                DESCRIPTION: Occurs on June 20th. Yule marks the day
                shortest of the year. From now on, the days become
                longer and we celebrate the return of the sun to earth.
                The date is also known as Alban Altha.
                SEASON: WINTER SOLSTICE''')
                print('-=-'*40)
                print('''IMBOLC >>>>>>>> START DAY: AUGUST 1
                END DAY: AUGUST 2
                DESCRIPTION: Feast of Fire, Sun and Light
                is celebrated on the 1st of August. Imbolc is a festival that,
                in many traditions, it celebrates the Celtic goddess Brigid.
                The date marks the middle between winter and spring,
                establishing itself as a festival of purification, light,
                fertility and new beginnings.''')
                print('-=-'*40)
                print('''OSTARA >>>>>>>> START DAY: SEPTEMBER 20
                END DAY: SEPTEMBER 23
                DESCRIPTION: Feast of fertility, takes place on September 20th.
                Ostara is a time to prepare for the start of a
                new life. The hours of day and night are the same, and the
                light surpasses the darkness. It is also known as Alban Eilir.
                SEASON: SPRING EQUINOX.''')
                print('-=-'*40)
                print('''BELTANE >>>>>>> START DAY: OCTOBER 31
                END DAY: NOVEMBER 1
                DESCRIPTION: Spring Festival is celebrated on October 31st.
                Beltane is a festival that honors the fertility of the land.
                It consists of a time of lust, passion, fire and abundance.''')
                print('-=-'*40)
                print('''LITHA >>>>>>>>> START DAY: DECEMBER 20
                END DAY: DECEMBER 23
                DESCRIPTION: Occurs on December 20th.
                Litha marks the longest day of the year. It's a celebration of
                triumph of light over darkness, and of the abundant beauty
                that light gives to our lives. It is also known as Alban Hefin.
                SEASON: SUMMER SOLSTICE.\33[m''')
            elif name != NomeRDA:
                break
            resp = str(input('\33[1;35mContinue? {Y/N}:')).strip().upper()[0]
            if resp in 'N':
                break
            elif resp not in 'YN':
                break
        if local == 'HN':
            print('\33[1;31mCHOICE:')
            print('IMBOLC,', 'OSTARA,', 'BELTANE,', 'LITHA,')
            print('-'*30)
            print('LAMMAS,', 'MABON,', 'SAMHAIN,', 'YULE,', ' ALL.\33[m')
            name = str(input('\33[1;35mChoose a date: ')).strip().upper()
            if name == 'IMBOLC':
                print(f'''{name} >>>>>>>> START DAY: 1 FEBRUARY
                END DAY: FEBRUARY 2
                DESCRIPTION: Feast of Fire, Sun and Light
                is celebrated on the 1st of February. Imbolc is a festival
                that, in many traditions, it celebrates the Celtic goddess
                Brigid. The date marks the middle between winter and spring,
                establishing itself as a festival of purification, light,
                fertility and new beginnings.''')
            elif name == 'OSTARA':
                print(f'''{name} >>>>>>>> START DAY: MARCH 17
                END DAY: MARCH 22
                DESCRIPTION: Feast of fertility, takes place on March 17th.
                Ostara is a time to prepare for the start of a
                new life. The hours of day and night are the same, and the
                light surpasses the darkness. It is also known as Alban Eilir.
                SEASON: SPRING EQUINOX''')
            elif name == 'BELTANE':
                print(f'''{name} >>>>>>> START DAY: APRIL 30
                END DAY: APRIL 30
                DESCRIPTION: Spring Festival is celebrated on April 30th.
                Beltane is a festival that honors the fertility of the land.
                It consists of a time of lust, passion, fire and abundance.''')
            elif name == 'LITHA':
                print(f'''{name} >>>>>>>>> START DAY: JUNE 21
                END DAY: JULY 01
                DESCRIPTION: Occurs on June 21st.
                Litha marks the longest day of the year. It's a celebration of
                triumph of light over darkness, and of the abundant beauty that
                light provides to our lives. It is also known as
                Alban Hefin.
                SEASON: SUMMER SOLSTICE''')
            elif name == 'LAMMAS':
                print(f'''{name} >>>>>>>> START DATE: AUGUST 1
                END DATE: AUGUST 2
                DESCRIPTION: Harvest festival, celebrated on August 1st.
                Pronounced lammas, this is a festival that honors
                the god Lugh. It celebrates the beginning of the harvest
                period for the grains. This is the first harvest festival,
                when the plants drop their seeds to ensure the cycle.''')
            elif name == 'MABON':
                print(f'''{name} >>>>>>>>> START DATE: SEPTEMBER 21
                END DATE: SEPTEMBER 29
                DESCRIPTION: It takes place on the 21st of September.
                Mabon is a moment thanksgiving celebration that celebrates
                the second harvest, the days and the nights are the same again,
                but the night keeps growing increasingly. Also known as Alban
                Elfed (the Light of Water).
                SEASON: AUTUMN EQUINOX,''')
            elif name == 'SAMHAIN':
                print(f'''{name} >>>>>>> START DAY: OCTOBER 31
                END DAY: OCTOBER 31
                DESCRIPTION: It is the Celtic New Year, it takes place on
                October 31st. Pronounced Sou-Em, represents the final harvest
                that precedes a long winter. It's time to honor our ancestors
                and embrace the darkest half of the year. Samhain too
                mark the beginning of the New Year in many Pagan
                traditions.''')
            elif name == 'YULE':
                print(f'''{name} >>>>>>>>>> START DAY: DECEMBER 21
                END DAY: DECEMBER 23
                DESCRIPTION: Occurs on December 21st. Yule marks the day
                shortest of the year. From now on, the days become
                longer and we celebrate the return of the sun to earth.
                The date is also known as Alban Altha.
                SEASON: WINTER SOLSTICE''')
            elif name == 'ALL':
                print('''IMBOLC >>>>>>>> START DAY: 1 FEBRUARY
                END DAY: FEBRUARY 2
                DESCRIPTION: Feast of Fire, Sun and Light
                is celebrated on the 1st of February. Imbolc is a festival
                that, in many traditions, it celebrates the Celtic goddess
                Brigid. The date marks the middle between winter and spring,
                establishing itself as a festival of purification, light,
                fertility and new beginnings.''')
                print('-=-'*40)
                print('''OSTARA >>>>>>>> START DAY: MARCH 17
                END DAY: MARCH 22
                DESCRIPTION: Feast of fertility, takes place on March 17th.
                Ostara is a time to prepare for the start of a
                new life. The hours of day and night are the same, and the
                light surpasses the darkness. It is also known as Alban Eilir.
                SEASON: SPRING EQUINOX''')
                print('-=-'*40)
                print('''BELTANE >>>>>>> START DAY: APRIL 30
                END DAY: APRIL 30
                DESCRIPTION: Spring Festival is celebrated on April 30th.
                Beltane is a festival that honors the fertility of the land.
                It consists of a time of lust, passion, fire and abundance.''')
                print('-=-'*40)
                print('''LITHA >>>>>>>>> START DAY: JUNE 21
                END DAY: JULY 01
                DESCRIPTION: Occurs on June 21st.
                Litha marks the longest day of the year. It's a celebration of
                triumph of light over darkness, and of the abundant beauty that
                light provides to our lives. It is also known as
                Alban Hefin.
                SEASON: SUMMER SOLSTICE''')
                print('-=-'*40)
                print('''LAMMAS >>>>>>>> START DATE: AUGUST 1
                END DATE: AUGUST 2
                DESCRIPTION: Harvest festival, celebrated on August 1st.
                Pronounced lammas, this is a festival that honors
                the god Lugh. It celebrates the beginning of the harvest
                period for the grains. This is the first harvest festival,
                when the plants drop their seeds to ensure the cycle.''')
                print('-=-'*40)
                print('''MABON >>>>>>>>> START DATE: SEPTEMBER 21
                END DATE: SEPTEMBER 29
                DESCRIPTION: It takes place on the 21st of September.
                Mabon is a moment thanksgiving celebration that celebrates
                the second harvest, the days and the nights are the same again,
                but the night keeps growing increasingly. Also known as Alban
                Elfed (the Light of Water).
                SEASON: AUTUMN EQUINOX,''')
                print('-=-'*40)
                print('''SAMHAIN >>>>>>> START DAY: OCTOBER 31
                END DAY: OCTOBER 31
                DESCRIPTION: It is the Celtic New Year, it takes place on
                October 31st. Pronounced Sou-Em, represents the final harvest
                that precedes a long winter. It's time to honor our ancestors
                and embrace the darkest half of the year. Samhain too
                mark the beginning of the New Year in many Pagan
                traditions.''')
                print('-=-'*40)
                print('''YULE >>>>>>>>>> START DAY: DECEMBER 21
                END DAY: DECEMBER 23
                DESCRIPTION: Occurs on December 21st. Yule marks the day
                shortest of the year. From now on, the days become
                longer and we celebrate the return of the sun to earth.
                The date is also known as Alban Altha.
                SEASON: WINTER SOLSTICE''')
            elif name != NomeRDA2:
                break
            resp = str(input('Continue? {Y/N}: \33[m')).strip().upper()[0]
            if resp in 'N':
                break
            elif resp not in 'YN':
                break
    elif local != 'HSHN':
        break
print('\33[1;34mSEJA SEMPRE BEM VINDO, RODA DO ANO COMPLETA\33[m')
print('\33[1;34m WELCOME ALWAYS, COMPLETE WHEEL OF THE YEAR\33[m')
