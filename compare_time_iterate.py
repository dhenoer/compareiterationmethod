import time
import random

class StopWatch:
    '''class stopwatch
    calculate time elapsed between start and stop in seconds
    '''

    def __init__(self):
        self.start()
        self._stop = 0

    def start(self):
        '''start stopwatch'''
        self._start = time.time()

    def restart(self):
        '''restart stopwath'''
        self.start()

    def stop(self):
        '''stop stopwatch. elapsed will be counted based on stop time'''
        self._stop = time.time()

    def elaps(self):
        '''return elapsed time in seconds'''
        if self._stop:
            return(self._stop - self._start)
        else:
            return(time.time()-self.start)

class RekapProses:
    ''' class RekapProses
    merekam dan mencatat waktu proses dari mulai sampai stop
    '''
    def __init__(self):
        self._time_record = {}
        self._sw = StopWatch()
        self._label = ''
        self._cases = 0
        self._trials = 0

    def mulai(self, metode):
        '''mulai proses'''
        self._label = metode
        self._sw.start()

    def selesai(self, data):
        '''catat hasil / waktu proses'''
        self._sw.stop()
        if self._label:
            print('# __ Iterasi',self._label,'__')
            print('Top5 =', data[:5], '...')
            print('Waktu =',self._sw.elaps(),'seconds\n')
            self._time_record[self._label] = self._time_record.get(self._label,0) + self._sw.elaps()
            self._cases += len(data)
            self._trials += 1
            self._label = '' #reset
        else:
            print('Rekap belum pernah dimulai')

    def hasil(self):
        '''menampilkan hasil / summary'''
        print('# Hasil Rekap Waktu (seconds) dan Speed')
        lenlabel = max([len(x) for x in self._time_record.keys()])
        maxtime = max([x for x in self._time_record.values()])
        for tk,tv in self._time_record.items():
            speed = maxtime / tv
            print(tk.ljust(lenlabel),'=', '%4.6f'%tv,
                ('*'*int(20*tv/maxtime)).ljust(20), '%3.1fx'%speed)
        print('Banyaknya data:', self._cases)
        print('Banyaknya trial:', self._trials//len(self._time_record.items()), '\n')

def metode(m):
    '''coding beberapa metode disini'''

    if m == 1:
        # mulai baca kolom 2 dg metode 1
        data_copy = []
        rekap.mulai('Metode Satu')
        for i in range(len(data)):
            data_copy.append(data[i][1])
        rekap.selesai(data_copy)

    elif m == 2:
        # mulai baca kolom 2 dg metode 2
        data_copy = []
        rekap.mulai('Metode Dua')
        for d in data:
            data_copy.append(d[1])
        rekap.selesai(data_copy)

    elif m == 3:
        # mulai baca kolom 2 dg metode 3
        rekap.mulai('Metode Tiga')
        data_copy = [data[i][1] for i in range(len(data))]
        rekap.selesai(data_copy)

    elif m == 4:
        # mulai baca kolom 2 dg metode 4
        rekap.mulai('Metode Empat')
        data_copy = [ d[1] for d in data]
        rekap.selesai(data_copy)

    else:
        print('Metode tidak ditemukan')


if __name__ == '__main__':

    print('Membandingkan waktu yang dibutuhkan untuk iterasi')
    print('beberapa metode / gaya pemrograman\n')

    # tentukan random seed untuk menghasilkan output yg sama
    random.seed('coba')

    # siapkan rekap
    rekap = RekapProses()

    # trial several times
    trial = random.randint(1,50)
    for t in range(trial):

        print('## TRIAL', t+1, '/',trial,'##\n')

        # generate random data
        size = random.randint(1,900)*1000
        #size = 1000000
        print('# Generating sample data ukuran=',size,'baris, tunggu ya...')
        data = []
        for _ in range(size):
            d0 = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for n in range(5)])
            d1 = random.randint(1e5,1e7)
            data.append([d0, d1])

        print('Data Top5 =', data[:5], '...\n')

        # acak metode
        mets = [1,2,3,4]
        random.shuffle(mets)
        for m in mets:
            metode(m)

    # hasilnya ..
    rekap.hasil()